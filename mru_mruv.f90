program mru_mruv
  implicit none

  ! Variáveis de entrada
  real :: x0, v0, a, t, dt, tf
  integer :: i, n
  character(len=4) :: tipo

  ! Variáveis de saída
  real :: x, v

  ! Entrada de dados
  print *, 'Escolha o tipo de movimento: MRU ou MRUV'
  read(*,*) tipo

  print *, 'Digite a posição inicial (x0):'
  read(*,*) x0

  print *, 'Digite a velocidade inicial (v0):'
  read(*,*) v0

  if (trim(tipo) == 'MRUV') then
     print *, 'Digite a aceleracao (a):'
     read(*,*) a
  else
     a = 0.0
  end if

  print *, 'Digite o tempo final (s):'
  read(*,*) tf

  print *, 'Digite o passo de tempo (dt):'
  read(*,*) dt

  ! Inicialização
  n = int(tf/dt)

  print *, 'Tempo (s)', '   Posicao (m)', '   Velocidade (m/s)'

  ! Loop de simulação
  do i = 0, n
     t = i * dt

     if (trim(tipo) == 'MRU') then
        x = x0 + v0 * t
        v = v0
     else if (trim(tipo) == 'MRUV') then
        x = x0 + v0 * t + 0.5 * a * t**2
        v = v0 + a * t
     else
        print *, 'Tipo de movimento invalido!'
        stop
     end if

     print '(F6.2, 3X, F10.4, 3X, F10.4)', t, x, v
  end do

end program mru_mruv