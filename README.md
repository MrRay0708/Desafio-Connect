# Desafio-Connect

## Introdução
Este repositório tem como finalidade importar e apresentar o workflow desenvolvido no windmill.dev para o desafio da Connect. <br>
A Função do Workflow é autenticar um documento CNH e validá-lo através da verificação de seus dados e da autenticidade visual do usuário com as fotos de identidade apresentadas.

## Instruções
O Workflow é armazenado dentro da pasta "u/henriquelfs2". para execução do projeto é necessário exportar as componentes para um ambiente windmill e atentar-se ao path que direcionam, se possível inicalizr em um workspace com nome de usuário henriquelfs2 facilita a integração, se não deve ser substituido manualmente.
- Scripts que se encontram tanto em .py, quanto .yaml
- App AutenticadorCNH que servirá como interface
- Flows que servirão como orquestradores e devolverão os resultados necessários para o App

Também é necessário configurar a client_key como variável secreta com nome api_key, para que cada componente funcione ao adquirir um Token para fazer a chamada REST.

## Execução
Após a correta exportação dos arquivos, basta iniciar o App AutenticadorCNH que a própria interface os guiará para obter o resultado desejado. <br><br>
Detalhando mais a execução, o primeiro passo será enviar a imagem frontal da CNH para ser analisada via Content Extraction, aguardando o "Ok" aparecer para prosseguir, evitando a má execução do workflow independente do hardware ou conexão. Em seguida envie a imagem de verso para ser analisada pelo Vio Extraction. Por fim, no terceiro passo haverá um botão que acionará o Flow que cria uma sessão por meio do Liveness Streaming para autenticação visual. Quando executar esta ação, ocasionará na ativação de outro Flow por conta da criação de um sessionId, sendo que este verificará constantemente o status da sessão por meio do Liveness Streaming Status antes de prosseguir para as comparações via Face Comparisson. Ao finalizar este último Sub-Flow, teremos no final da página um resumo das informações apreendidas e o resultado das comparações de autenticidade, assim como uma avaliação geral sobre a similaridade visual.
