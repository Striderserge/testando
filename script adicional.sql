CREATE TABLE if NOT EXISTS tb_usuario(
id_usuario INT NOT NULL AUTO_INCREMENT,
email_usuario VARCHAR(300) NOT NULL,
senha_usuario VARCHAR(20) NOT NULL,
PRIMARY KEY (`id_usuario`)
);

ALTER TABLE tb_paciente
ADD COLUMN id_usuario INT NOT NULL;

ALTER TABLE tb_paciente
ADD CONSTRAINT fkusuario FOREIGN KEY(id_usuario) REFERENCES tb_usuario(id_usuario);

ALTER TABLE tb_agendamento
ADD CONSTRAINT fkusuario FOREIGN KEY(id_usuario) REFERENCES tb_usuario(id_usuario);