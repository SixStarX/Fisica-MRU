program mru_mruv
  implicit none

  real :: x0, v0, a, t, dt, tf
  integer :: i, n
  character(len=4) :: tipo
  real :: x, v
  integer :: unit

  ! Unidade de arquivo
  unit = 10

  ! Entrada interativa
  print *, 'Digite o tipo de movimento (MRU ou MRUV):'
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

  n = int(tf/dt)

  ! Abrir arquivo para saída
  open(unit=unit, file='dados.txt', status='replace')

  ! Escrever cabeçalho (opcional)
  write(unit,*) 'Tempo  Posicao  Velocidade'

  ! Loop de cálculo e gravação
  do i = 0, n
     t = i * dt
     if (trim(tipo) == 'MRU') then
        x = x0 + v0 * t
        v = v0
     else
        x = x0 + v0 * t + 0.5 * a * t**2
        v = v0 + a * t
     end if
     write(unit,'(F6.2,1X,F10.4,1X,F10.4)') t, x, v
  end do

  close(unit)
  print *, '✅ Dados gravados com sucesso em dados.txt'

end program mru_mruv