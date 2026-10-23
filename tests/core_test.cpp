#include <cassert>
#include <fstream>
#include <iterator>
#include <vector>
#include "../native/core.hpp"
int main(){
    std::vector<uint8_t> cells(MAP_W*MAP_H,0);
    Explorer p(cells.data());
    p.x=100;p.y=100;p.update(1,0,.05f,false);float straight=p.x-100;
    p.x=100;p.y=100;p.update(1,1,.05f,false);
    assert(std::abs(std::hypot(p.x-100,p.y-100)-straight)<.0001f);
    cells[6*MAP_W+7]=1;p.x=107;p.y=105;
    for(int n=0;n<100;++n)p.update(1,0,.05f,true);
    assert(p.x<108); // right-hand corners may not enter a blocked tile at x=112
    p.x=5;p.y=105;for(int n=0;n<10;++n)p.update(-1,0,.05f,true);assert(p.x>=4);
    assert(p.blocked(-.01f,0));assert(p.blocked(MAP_W*TILE,0));
    float old=p.x;p.update(1,0,-1,false);assert(p.x==old);
    if(std::ifstream file("assets/collision.bin",std::ios::binary);file){
        std::vector<uint8_t> actual((std::istreambuf_iterator<char>(file)),{});
        assert(actual.size()==MAP_W*MAP_H);Explorer real(actual.data());assert(real.canMove(real.x,real.y));
    }
}
