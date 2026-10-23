// Experimental WUT software renderer. No Wii U build or hardware validation yet.
#include <coreinit/cache.h>
#include <coreinit/memory.h>
#include <coreinit/screen.h>
#include <coreinit/thread.h>
#include <coreinit/time.h>
#include <vpad/input.h>
#include <whb/proc.h>
#include <malloc.h>
#include <cstdio>
#include <cstdlib>
#include "core.hpp"
#include "farm_ground_bin.h"
#include "farm_front_bin.h"
#include "avatar_bin.h"
#include "collision_bin.h"

constexpr int WORLD_W=MAP_W*TILE,WORLD_H=MAP_H*TILE;
static uint32_t rgb(const uint8_t* pixel){return uint32_t(pixel[0])<<24|uint32_t(pixel[1])<<16|uint32_t(pixel[2])<<8;}
static uint32_t over(uint32_t background,const uint8_t* pixel){
    unsigned a=pixel[3];if(a==0)return background;if(a==255)return rgb(pixel);
    uint32_t out=0;
    for(int c=0;c<3;++c){int shift=24-c*8;unsigned b=(background>>shift)&255;out|=((pixel[c]*a+b*(255-a)+127)/255)<<shift;}
    return out;
}
static uint32_t worldPixel(int wx,int wy,const Explorer& player,bool avatar){
    if(wx<0||wy<0||wx>=WORLD_W||wy>=WORLD_H)return 0;
    int offset=(wy*WORLD_W+wx)*4;
    uint32_t pixel=rgb(farm_ground_bin+offset);
    if(avatar){
        int px=int(player.x)-8,py=int(player.y)-28,sx=wx-px,sy=wy-py;
        if(sx>=0&&sx<16&&sy>=0&&sy<32){
            if(player.direction==3)sx=15-sx;
            int row=player.direction==0?0:player.direction==2?2:1;
            int frame=player.walk>0?int(player.walk)%4:0;
            pixel=over(pixel,avatar_bin+((row*32+sy)*64+frame*16+sx)*4);
        }
    }
    return over(pixel,farm_front_bin+offset);
}
static void draw(OSScreenID screen,const Explorer& player,bool map){
    // Deliberately small validation viewport; GPU rendering is a later milestone.
    const int vw=320,vh=180,scale=2;
    int cx=std::clamp(int(player.x)-vw/2,0,WORLD_W-vw);
    int cy=std::clamp(int(player.y)-vh/2,0,WORLD_H-vh);
    OSScreenClearBufferEx(screen,0x111c2400);
    for(int y=0;y<vh;++y)for(int x=0;x<vw;++x){
        int wx=map?x*WORLD_W/vw:cx+x,wy=map?y*WORLD_H/vh:cy+y;
        uint32_t colour=worldPixel(wx,wy,player,!map);
        if(map&&std::abs(wx-int(player.x))<7&&std::abs(wy-int(player.y))<7)colour=0xffffff00;
        for(int yy=0;yy<scale;++yy)for(int xx=0;xx<scale;++xx)
            OSScreenPutPixelEx(screen,32+x*scale+xx,64+y*scale+yy,colour);
    }
    OSScreenPutFontEx(screen,0,0,screen==SCREEN_TV?"Stardew exploration v0.1 - EXPERIMENTAL":"GamePad: Y = map / game");
    OSScreenPutFontEx(screen,0,1,"Stick/D-pad move | A run | X reset | + exit");
}
int main(){
    WHBProcInit();OSScreenInit();
    uint32_t size[2]={OSScreenGetBufferSizeEx(SCREEN_TV),OSScreenGetBufferSizeEx(SCREEN_DRC)};
    void* buffers[2]={memalign(0x100,size[0]),memalign(0x100,size[1])};
    if(!buffers[0]||!buffers[1]){free(buffers[0]);free(buffers[1]);OSScreenShutdown();WHBProcShutdown();return 1;}
    for(int i=0;i<2;++i){OSScreenSetBufferEx(OSScreenID(i),buffers[i]);OSScreenEnableEx(OSScreenID(i),TRUE);}
    Explorer player(collision_bin);bool padMap=true;
    auto previous=OSGetTime();
    while(WHBProcIsRunning()){
        auto now=OSGetTime();float dt=float(OSTicksToMicroseconds(now-previous))/1000000.f;previous=now;
        VPADStatus input{};VPADReadError error;
        int count=VPADRead(VPAD_CHAN_0,&input,1,&error);
        if(count>0&&error==VPAD_READ_SUCCESS){
            if(input.trigger&VPAD_BUTTON_PLUS)break;
            if(input.trigger&VPAD_BUTTON_Y)padMap=!padMap;
            if(input.trigger&VPAD_BUTTON_X)player.reset();
            float dx=std::abs(input.leftStick.x)>.2f?input.leftStick.x:0;
            float dy=std::abs(input.leftStick.y)>.2f?-input.leftStick.y:0;
            dx+=bool(input.hold&VPAD_BUTTON_RIGHT)-bool(input.hold&VPAD_BUTTON_LEFT);
            dy+=bool(input.hold&VPAD_BUTTON_DOWN)-bool(input.hold&VPAD_BUTTON_UP);
            player.update(dx,dy,dt,input.hold&VPAD_BUTTON_A);
        }else player.walk=0;
        draw(SCREEN_TV,player,false);draw(SCREEN_DRC,player,padMap);
        for(int i=0;i<2;++i){DCFlushRange(buffers[i],size[i]);OSScreenFlipBuffersEx(OSScreenID(i));}
        OSSleepTicks(OSMillisecondsToTicks(1));
    }
    for(int i=0;i<2;++i)OSScreenEnableEx(OSScreenID(i),FALSE);
    OSScreenShutdown();free(buffers[0]);free(buffers[1]);WHBProcShutdown();return 0;
}
