integer :: ios

! Leitura com verificação
read(in,*,IOSTAT=ios) tipo
if (ios /= 0) stop 'Erro ao ler tipo'

read(in,*,IOSTAT=ios) x0
if (ios /= 0) stop 'Erro ao ler x0'

read(in,*,IOSTAT=ios) v0
if (ios /= 0) stop 'Erro ao ler v0'

read(in,*,IOSTAT=ios) a
if (ios /= 0) stop 'Erro ao ler a'

read(in,*,IOSTAT=ios) tf
if (ios /= 0) stop 'Erro ao ler tf'

read(in,*,IOSTAT=ios) dt
if (ios /= 0) stop 'Erro ao ler dt'