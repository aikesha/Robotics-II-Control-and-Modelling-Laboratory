function T = Rototr(q, L)
%     length(q);
%     length(L);
    T = eye(4);
    
    for i = 1:length(q)
        ct = cos(q(i));
        st = sin(q(i));
        ca = cos(0);
        sa = sin(0);
        T = T*[ ct    -st*ca   st*sa    L(i)*ct ; ...
                st    ct*ca    -ct*sa    L(i)*st ; ...
                0     sa       ca           0; ...
                0     0        0            1];
        
    end
end