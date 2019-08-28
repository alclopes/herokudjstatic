# Deploy de Aplicação Django no Heroku - TestHeroku V2

Conheça a aplicação no [Heroku](https://alclopes-test.herokuapp.com/).

## Características básicas desta aplicação
##### 01. Aplicação de página unica
##### 02. Uso de Imagem Estática
##### 03. Opção de Upload de Mídia (media - POST de imagem)
##### 04. Biblioteca DeCouple para proteger as variáveis de configuração
##### 05. Uso de Whitenoise apenas no ambiente de produção
##### 06. Gestão dos Settings de produção e desenvolvimento separados
##### 07. Gestão dos Requirements de produção e desenvolvimento separados
##### 08. Uso de signals para excluir arquivos de media no servidor quando ultrapasa o limite de três imagens
##### 09. Validação da disponibilidade de arquivos de media no servidor e posterior exclusão da referência em BD na ausência do arquivo.

## Lembretes e cuidados importantes ao utilizar o Heroku
##### 01. Importante para não ter retrabalho é saber que a base de dados utilizada pelo Heroku é o Postgres
* O Heroku utiliza o Postgres como base de dados padrão, portanto, se estiver utilizando db.sqlite3 para desenvolvimento em sua maquina local, você dever apagar e recriar suas migrações para postgres antes de fazer o deploy no servidor.
##### 02. Lembre-se na opção grátis o Heroku não armazena seus uploads
* Imagens de origem de upload (pasta MEDIA da aplicação) não são mantidas pelo HEROKU (uma solução é usar amazon S3 para armazená-las)
* Motivos do Heroku apagar os arquivos media: o Servidor de imagens não exige complexidade podendo até ser um servidor apache e também para evitar sobrecarga de arquivos no servidor gratis e portanto a queda de sua performance a longo prazo.
* Não estou utilizando um servidor de arquivos estáticos externos neste projeto e o heroku apaga os arquivos físicos, portanto, criei uma condição para apagar os registros na base de dados referentes a estes arquivos deletados (não há regra de negócio envolvida aos registros). Em breve irei incluir outro projeto utilizando o S3.
##### 03. Importante tentar controlar o armazenamento por upload de sua aplicação 
* Como não vou controlar o conteúdo dos uploads limitei a apenas 3 imagens (media) disponíveis no servidor, 
* Também coloquei as imagens em um percentual de tamanho de 2% o que não permite a visibilidade clara da imagem na própria página.

## Algumas dicas para rodar a aplicação
 Além das dicas usuais de instalação utilizando o GIT,  seguir as dicas abaixo:
#### Valorizar as variáveis de configuração abaixo:
 
##### 1. Para rodar a aplicação setar no arquivo .env ou .ini criado para o pacote decouple as variáveis:
            SECRET_KEY=... 
            DEBUG=True
            SETTINGS_MODULE_PATH=testheroku.settings.development
            DEBUG_DESENV=True 
            ALLOWED_HOSTS_DEV =.localhost,127.0.0.1
            
##### 2. Para rodar a aplicação setar no ambiente do heroku as variáveis:
            SECRET_KEY=... 
            DEBUG=False
            ALLOWED_HOSTS=.herokuapp.com 
            SETTINGS_MODULE_PATH=testheroku.settings.production
            DISABLE_COLLECTSTATIC=1
            DATABASE_URL=...   #Será incluida e configurada automaticamente pelo Heroku na inclusão do Resource/addon do Postgres
              
## Teste Heroku - Situação Atual do projeto
##### 1. Deploy de pequena aplicação Django no Heroku 
=> Situação: Feito/Sucesso
##### 2. Gestão de arquivos estáticos 
=> Situação: Pendente (mais detalhes abaixo) 
##### 3. Gestão de arquivos média 
=> Situação: Feito/Sucesso (mais detalhes abaixo)

## Branch02 - V2-Heroku-Dj-static
##### Pacote: dj-static
* Promete a gerencia de arquivos estáticos no servidor
* Configuração simples

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos - Situação: Aguardando Solução
* Envolveu: Imagens e CSS
* Se Debug = False não esta servindo arquivos estáticos 
* Se Debug = True - OK

##### 2. Upload de Arquivos de Mídia (media) - Situação: OK
* Envolveu imagens por upload do usuário
* Se Debug = False - OK
* Se Debug = True - OK

## Branch01 - V1-Heroku-Whitenoise
##### Pacotes: Whitenose 4.1.2 + django_heroku 0.3.1
* Promete a gerencia de arquivos estáticos no servidor
* "WhiteNoise is not suitable for serving user-uploaded “media” files." Source:WhiteNoise

#### Detalhes da Situação do Projeto Teste

##### 1. Arquivos estáticos - Situação: Aguardando Solução
* Envolveu: Imagens e CSS
* Se Debug = False dá erro 500
* Se Debug = True - OK

##### 2. Upload de Arquivos de Mídia (media) - Situação: Aguardando Solução
* Envolveu imagens por upload do usuário
* Se Debug = False dá erro 500
* Se Debug = True - OK
  
####  Lembretes e cuidados importantes ao utilizar o Django com WhiteNoise
* As part of deploying your application you’ll need to run ./manage.py collectstatic to put all your static files into STATIC_ROOT. (If you’re running on Heroku then this is done automatically for you.)
* You might find other third-party middleware that suggests it should be given highest priority at the top of the middleware list. Unless you understand exactly what is happening you should ignore this advice and always place WhiteNoiseMiddleware above other middleware. If you plan to have other middleware run before WhiteNoise you should be aware of the request_finished bug in Django.
