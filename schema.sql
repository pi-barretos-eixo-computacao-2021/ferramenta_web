CREATE TABLE controle_ferias (
    ID                 INTEGER        NOT NULL,
    inclusao           DATETIME       NOT NULL
                                      DEFAULT CURRENT_TIMESTAMP,
    empresaid          INTEGER (3)    NOT NULL,
	pessoa 			   VARCHAR (60)	  NOT NULL,
    data_inicio_ferias DATE           NOT NULL,
    data_fim_ferias    DATE           NOT NULL,
    valor_ferias       DECIMAL (6, 2) NOT NULL,
    PRIMARY KEY (
        ID AUTOINCREMENT
    )	
);