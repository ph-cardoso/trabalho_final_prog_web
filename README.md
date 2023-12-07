# Projeto Final da disciplina Programação para web

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como Rodar o Projeto

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/ph-cardoso/trabalho_final_prog_web.git
   cd trabalho_final_prog_web
   ```

2. **Configuração do Ambiente:**

   É possível rodar o ambiente sem configurar um arquivo `.env` apenas utilizando os valores default. Caso queira / precise mudar algo, crie um arquivo chamado `.env` na raiz do projeto e configure as variáveis de ambiente necessárias. 

   Um exemplo pode ser encontrado no arquivo `.env.example`.

3. **Inicie os Contêineres:**

   Execute o seguinte comando para construir e iniciar os contêineres do Docker:

   ```bash
   docker-compose up -d
   ```

   Isso iniciará os contêineres necessários, incluindo o MySQL e o FastAPI.

4. **Acesso à Aplicação:**

   Após a inicialização bem-sucedida, a aplicação estará acessível em [http://localhost:8000](http://localhost:8000). Certifique-se de substituir a porta conforme necessário com base nas configurações do seu ambiente.

   A documentação se encontra em:

   [http://localhost:8000/docs](http://localhost:8000/docs)

5. **Parar os Contêineres:**

   Para encerrar a execução dos contêineres, utilize o seguinte comando:

   ```bash
   docker-compose down
   ```

   Isso encerrará os contêineres e liberará os recursos.

Lembre-se de ajustar as configurações conforme necessário com base nas suas preferências e requisitos específicos do projeto.
