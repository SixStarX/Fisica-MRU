program massa_mola_amortecido
  implicit none

  ! Parâmetros físicos
  real :: m, k, c             ! massa, constante da mola, amortecimento
  real :: x, v                ! posição e velocidade
  real :: t, dt, tf           ! tempo atual, passo de tempo, tempo final
  integer :: n, i

  ! Variáveis auxiliares para RK4
  real :: k1x, k2x, k3x, k4x
  real :: k1v, k2v, k3v, k4v
  real :: a                   ! aceleração temporária

  ! Inicialização dos parâmetros
  m  = 1.0        ! kg
  k  = 10.0       ! N/m
  c  = 0.5        ! kg/s
  x  = 1.0        ! posição inicial (m)
  v  = 0.0        ! velocidade inicial (m/s)
  t  = 0.0        ! tempo inicial (s)
  dt = 0.01       ! passo de tempo (s)
  tf = 10.0       ! tempo final (s)

  n = int(tf/dt)

  ! Cabeçalho da saída
  print *, 'Tempo (s)', 'Posição (m)', 'Velocidade (m/s)'

  ! Loop de simulação
  do i = 1, n
     ! Runge-Kutta 4ª ordem

     k1x = dt * v
     k1v = dt * (- (c/m)*v - (k/m)*x)

     k2x = dt * (v + 0.5*k1v)
     k2v = dt * (- (c/m)*(v + 0.5*k1v) - (k/m)*(x + 0.5*k1x))

     k3x = dt * (v + 0.5*k2v)
     k3v = dt * (- (c/m)*(v + 0.5*k2v) - (k/m)*(x + 0.5*k2x))

     k4x = dt * (v + k3v)
     k4v = dt * (- (c/m)*(v + k3v) - (k/m)*(x + k3x))

     x = x + (k1x + 2.0*k2x + 2.0*k3x + k4x) / 6.0
     v = v + (k1v + 2.0*k2v + 2.0*k3v + k4v) / 6.0
     t = t + dt

     print '(F8.3,2X,F10.5,2X,F10.5)', t, x, v
  end do
end program massa_mola_amortecido