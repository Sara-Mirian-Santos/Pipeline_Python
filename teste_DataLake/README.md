MinIO - Serviço de Armazenamento S3 Local

Este repositório configura e executa uma instância local do **MinIO**, um serviço de armazenamento de objetos compatível com S3, ideal para testes e desenvolvimento de pipelines de dados ou aplicações em nuvem.

## Arquitetura
1. **Python (ETL)** → scripts versionados no GitHub.
2. **Jenkins** → builda, testa e empacota em `.zip`.
3. **Upload para MinIO** → Jenkins faz o upload do artefato para o bucket `dags-dev`.

## Pré-requisitos

* Docker instalado
* Docker Compose
* Java 17
* Jenkins

## Preparando o Jenkins para se comunicar com o MinIO

```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/
```

**Verifique se funciona:**

```bash
mc --version
```

---

## Configurar credenciais no Jenkins

No Jenkins:

* Vá em: `Manage Jenkins > Credentials > Global > Add credentials`.
* Escolha **Username with password**.
* Preencha:

  * **ID**: `minio-creds`
  * **Username**: `admin`
  * **Password**: `admin123`

---

## Como usar

### 1. Subir o MinIO

```bash
docker compose up -d
```

### 2. Acessar o Console Web

* Acesse via navegador: [http://localhost:9001](http://localhost:9001)
* Faça login com:

  * **Usuário:** `admin`
  * **Senha:** `admin123`

### 3. Crie o bucket `dags-dev` no console do MinIO.

### 4. Execute a esteira no Jenkins e verifique se o MinIO recebeu o artefato.
