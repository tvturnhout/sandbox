### Installation:

# Huur VM op Google VM:
install dokku on ubuntu
# Registreer domeinnaam:
DNS route de VM IP naar domeinnaam (Type: A Record, Host: @ (én eentje met * voor subdomains), Value: IP, TTL: zo kort mogelijk)
# Op Windows host:
.ssh map maken met key in file id_rsa
hostname: domeinnaam
check use virtual hostnaming for apps
# Ga naar IP of domeinnaam:
Webpagina verschijnt: In bovenste dokku vak (oakwood.host) key pasten
# In VM ssh:
dokku apps:create appnameappelsap
# Op Windows host in de git repo:
git remote add dokku dokku@oakwood.host:appnameappelsap
git push dokku


