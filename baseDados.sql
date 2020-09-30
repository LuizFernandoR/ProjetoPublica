create database projeto_publica;

create table cadastro_jogo(
    id_cad_jogo int not null primary key auto_increment,
    num_cad_jogo int not null,
    placar_cad_jogo int not null,
    min_temporada int not null,
    max_temporada int not null,
    quebra_recorde_min int not null,
    quebra_recorde_max int not null);
)
