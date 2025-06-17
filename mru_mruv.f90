program mru_mruv
   implicit none
   ! Variáveis
   real :: x0, v0, a, tf, dt, t, x, v
   integer :: n, i
   character(len=10) :: tipo

   ! Lê parâmetros do arquivo de entrada
   open(unit=10, file='entrada.txt', status='old')
   read(10,*) tipo
   read(10,*) x0
   read(10,*) v0
   read(10,*) a
   read(10,*) tf
   read(10,*) dt
   close(10)

   ! Se for MRU, zera aceleração
   if (trim(adjustl(tipo)) == 'MRU') a = 0.0

   n = int(tf/dt) + 1
   open(unit=20, file='dados.txt', status='replace')
   write(20,*) 'Tempo  Posicao  Velocidade'

   do i = 0, n-1
      t = i*dt
      if (trim(adjustl(tipo)) == 'MRU') then
         x = x0 + v0*t
         v = v0
      else
         x = x0 + v0*t + 0.5*a*t**2
         v = v0 + a*t
      end if
      write(20,'(F8.3,1X,F12.5,1X,F12.5)') t, x, v
   end do
   close(20)
end program mru_mruv
