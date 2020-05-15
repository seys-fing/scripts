%mainRoadDumping simula un sistema de amortiguamiento de segundo orden
%Seleccione  zeta y wn
%valores bajos de wn (wn<w0=5) filtran oscilaciones en el camino pero son de
%reacción lenta al escalón - pruebe wn=1,zeta=.1 y wn=10,zeta=.1
%zetas bajos hacen oscilar a ambas respuestas - pruebe wn=1,zeta=1 y
%wn=10,zeta=1
%zetas bajas en con wn=w0 lleva a resonancia




R=.2; %road height
w0=5; %road bumps freq
d=0.2; %diameter of the wheel on the picture
L=3.5*d; %lenght of the damper 
Ts=5; % step instant
M=wn/(2*sqrt(zeta^2-1))
T=10;%time horizon

c1=-zeta*wn+wn*sqrt(zeta^2-1);
c2=-zeta*wn-wn*sqrt(zeta^2-1);
us=[-d:.001:d]; %auxiliary for ploting the wheel
ts=[-2*d:.001:T];
for t0=0:.1:T
    display(['to=', num2str(t0)])
    H=(wn^2+2*zeta*j*w0)/((j*w0)^2+2*zeta*wn*j*w0+wn^2);
    A=abs(H);
    phi=angle(H);
    y=A*R*cos(w0*t0+phi);
    chasisY=[0,    3*d, 3*d, 2*d, 2*d,  d,  0, 0]+y+L;
    chasisX=[-2*d,-2*d, -d,   0,  2*d, 3*d,3*d,-2*d];
    
    road=R*cos(w0*(ts+t0));
    r0=R*cos(w0*(0-t0));
    wheel=sqrt(d^2-us.^2);
    dumper=[r0+d*1.2,y+L];
    
    subplot 211
    plot(ts,road,'k',us,wheel+r0+d*1.2,'b',us,-wheel+r0+d*1.2,'b',[0,0],dumper,'b',chasisX,chasisY,'r')
    axis('equal')
    %plot(us,wheel,'b',us,-wheel,'b')
    subplot 212
    step=(ts>(T-t0-Ts))*1.5*R;
    s0=(0>T-t0-Ts)*1.5*R;
    if(zeta==1)
        s=(1-exp(-wn*(Ts-T+t0))-wn*(Ts+t0-T)*exp(-wn*(Ts+t0-T)))*s0;
        s=s+(2*zeta/wn*(  wn*exp(-wn*(Ts-T+t0)) - wn*exp(-wn*(Ts+t0-T))  +wn^2*(Ts-T+t0)*  exp(-wn*(Ts+t0-T)) ))*s0;
    else
        s=(1+M*(exp(c1*(Ts+t0-T))/c1-exp(c2*(Ts+t0-T))/c2))*s0;
        s=s+2*zeta/wn*( M*(exp(c1*(Ts+t0-T))-exp(c2*(Ts+t0-T))) )*s0;
    end
    
    chasisY=[0,    3*d, 3*d, 2*d, 2*d,  d,  0, 0]+s+L;
    chasisX=[-2*d,-2*d, -d,   0,  2*d, 3*d,3*d,-2*d];

    dumper=[s0+d*1.2,s+L];
    plot(ts,step,'k',us,wheel+s0+d*1.2,'b',us,-wheel+s0+d*1.2,'b',[0,0],dumper,'b',chasisX,chasisY,'r')
    axis('equal')
    shg
    pause(0.01)
    end


