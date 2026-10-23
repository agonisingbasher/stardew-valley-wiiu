#pragma once
#include <algorithm>
#include <cmath>
#include <cstdint>
#include "scene_config.h"

struct Explorer {
    float x=START_X, y=START_Y, walk=0;
    int direction=0;
    const uint8_t* collision;
    explicit Explorer(const uint8_t* cells): collision(cells) {}
    void reset(){x=START_X;y=START_Y;walk=0;direction=0;}
    bool blocked(float px,float py) const {
        int tx=int(std::floor(px/TILE)),ty=int(std::floor(py/TILE));
        return tx<0||ty<0||tx>=MAP_W||ty>=MAP_H||collision[ty*MAP_W+tx];
    }
    bool canMove(float px,float py) const {
        return !blocked(px-4,py-5)&&!blocked(px+4,py-5)&&!blocked(px-4,py-1)&&!blocked(px+4,py-1);
    }
    void update(float dx,float dy,float dt,bool run){
        if(!std::isfinite(dx)||!std::isfinite(dy)||!std::isfinite(dt)||dt<=0)return;
        dt=std::min(dt,.05f);
        float length=std::hypot(dx,dy);
        if(length<.1f){walk=0;return;}
        dx/=std::max(1.0f,length);dy/=std::max(1.0f,length);
        direction=std::abs(dx)>std::abs(dy)?(dx>0?1:3):(dy>0?0:2);
        float speed=run?100:65;
        int steps=std::max(1,int(std::ceil(speed*dt/3)));
        for(int n=0;n<steps;++n){
            float nx=x+dx*speed*dt/steps,ny=y+dy*speed*dt/steps;
            if(canMove(nx,y))x=nx;
            if(canMove(x,ny))y=ny;
        }
        walk+=dt*9;
    }
};
