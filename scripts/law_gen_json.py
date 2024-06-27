import re
import json

# Texto da lei
texto_lei = """
LEI No 8.383, DE 30 DE DEZEMBRO DE 1991
Art. 1° Fica instituída a Unidade Fiscal de Referência (Ufir), como medida de valor e parâmetro de atualização monetária de tributos e de valores expressos em cruzeiros na legislação tributária federal, bem como os relativos a multas e penalidades de qualquer natureza.
§ 1° O disposto neste capítulo aplica-se a tributos e contribuições sociais, inclusive previdenciárias, de intervenção no domínio econômico e de interesse de categorias profissionais ou econômicas.
§ 2° É vedada a utilização da Ufir em negócio jurídico como referencial de correção monetária do preço de bens ou serviços e de salários, aluguéis ou royalties.
Art. 2° A expressão monetária da Ufir mensal será fixa em cada mês-calendário; e da Ufir diária ficará sujeita à variação em cada dia e a do primeiro dia do mês será igual à da Ufir do mesmo mês.
§ 1° O Ministério da Economia, Fazenda e Planejamento, por intermédio do Departamento da Receita Federal, divulgará a expressão monetária da Ufir mensal;
até o dia 1° de janeiro de 1992, para esse mês, mediante a aplicação, sobre Cr$ 126,8621, do Índice Nacional de Preços ao Consumidor (INPC) acumulado desde fevereiro até novembro de 1991, e do Índice de Preços ao Consumidor Ampliado (IPCA) de dezembro de 1991, apurados pelo Instituto Brasileiro de Geografia e Estatística (IBGE);
até o primeiro dia de cada mês, a partir de 1° de fevereiro de 1992, com base no IPCA.
§ 2° O IPCA, a que se refere o parágrafo anterior, será constituído por série especial cuja apuração compreenderá o período entre o dia 16 do mês anterior e o dia 15 do mês de referência.
§ 3° Interrompida a apuração ou divulgação da série especial do IPCA, a expressão monetária da Ufir será estabelecida com base nos indicadores disponíveis, observada precedência em relação àqueles apurados por instituições oficiais de pesquisa.
§ 4° No caso do parágrafo anterior, o Departamento da Receita Federal divulgará a metodologia adotada para a determinação da expressão monetária da Ufir.
§ 5° O Departamento da Receita Federal divulgará, com antecedência, a expressão monetária da Ufir diária, com base na projeção da taxa de inflação medida pelo índice de que trata o § 2° deste artigo.                    (Revogado pela lei nº 9.069, de 29.6.1995)
§ 6° A expressão monetária do Fator de Atualização Patrimonial (FAP), instituído em decorrência da Lei n° 8.200, de 28 de junho de 1991, será igual, no mês de dezembro de 1991, à expressão monetária da Ufir apurada conforme a alínea a do § 1° deste artigo.
§ 7° A expressão monetária do coeficiente utilizado na apuração do ganho de capital, de que trata a Lei n° 8.218, de 29 de agosto de 1991, corresponderá, a partir de janeiro de 1992, à expressão monetária da Ufir mensal.
Art. 3° Os valores expressos em cruzeiros na legislação tributária ficam convertidos em quantidade de Ufir, utilizando-se como divisores:
I o valor de Cr$ 215,6656, se relativos a multas e penalidades de qualquer natureza;
II o valor de Cr$ 126,8621, nos demais casos.
Art. 4° A renda e os proventos de qualquer natureza, inclusive os rendimentos e ganhos de capital, percebidos por pessoas físicas residentes ou domiciliadas no Brasil, serão tributados pelo imposto de renda na forma da legislação vigente, com as modificações introduzidas por esta lei.
Art. 5° A partir de 1° de janeiro do ano-calendário de 1992, o imposto de renda incidente sobre os rendimentos de que tratam os arts. 7°, 8° e 12 da Lei n° 7.713, de 22 de dezembro de 1988, será calculado de acordo com a seguinte tabela progressiva:
Art. 6° O imposto sobre os rendimentos de que trata o art. 8° da Lei n° 7.713, de 1988:
I - será convertido em quantidade de Ufir pelo valor desta no mês em que os rendimentos forem recebidos;
II - deverá ser pago até o último dia útil do mês subseqüente ao da percepção dos rendimentos.
Art. 7° Sem prejuízo dos pagamentos obrigatórios estabelecidos na legislação, fica facultado ao contribuinte efetuar, no curso do ano, complementação do imposto que for devido sobre os rendimentos recebidos.
Art. 8° O imposto retido na fonte ou pago pelo contribuinte, salvo disposição em contrário, será deduzido do apurado na forma do inciso I do art. 15 desta lei.
Art. 9° As receitas e despesas a que se refere o art. 6° da Lei n° 8.134, de 27 de dezembro de 1990, serão convertidas em quantidade de Ufir pelo valor desta no mês em que forem recebidas ou pagas, respectivamente.
Art. 10. Na determinação da base de cálculo sujeita à incidência mensal do imposto de renda poderão ser deduzidas:
I - a soma dos valores referidos nos incisos do art. 6° da Lei n° 8.134, de 1990;
II - as importâncias pagas em dinheiro a título de alimentos ou pensões, em cumprimento de acordo ou decisão judicial, inclusive a prestação de alimentos provisionais;
III - a quantia equivalente a quarenta Ufir por dependente;
III - a quantia equivalente a cem UFIR por dependente;                      (Redação dada pela Lei nº 9.069, de 29.6.1995)
IV - as contribuições para a Previdência Social da União, dos Estados, do Distrito Federal e dos Municípios;
V - o valor de mil Ufir, correspondente à parcela isenta dos rendimentos provenientes de aposentadoria e pensão, transferência para reserva remunerada ou reforma pagos pela Previdência Social da União, dos Estados, do Distrito Federal e dos Municípios, ou por qualquer pessoa jurídica de direito público interno, a partir do mês em que o contribuinte completar sessenta e cinco anos de idade.
Art. 11. Na declaração de ajuste anual (art. 12) poderão ser deduzidos:
I - os pagamentos feitos, no ano-calendário, a médicos, dentistas, psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais e hospitais, bem como as despesas provenientes de exames laboratoriais e serviços radiológicos;
II - as contribuições e doações efetuadas a entidades de que trata o art. 1° da Lei n° 3.830, de 25 de novembro de 1960, observadas as condições estabelecidas no art. 2° da mesma lei;
III - as doações de que trata o art. 260 da Lei n° 8.069, de 13 de julho de 1990;
IV - a soma dos valores referidos no art. 10 desta lei;
V - as despesas feitas com instrução do contribuinte e seus dependentes até o limite anual individual de seiscentos e cinqüenta Ufir.
§ 1° O disposto no inciso I:
a) aplica-se, também, aos pagamentos feitos a empresas brasileiras ou autorizadas a funcionar no País, destinados à cobertura de despesas com hospitalização e cuidados médicos e dentários, bem como a entidades que assegurem direito de atendimento ou ressarcimento de despesas de natureza médica, odontológica e hospitalar;
b) restringe-se aos pagamentos feitos pelo contribuinte, relativos ao seu próprio tratamento e ao de seus dependentes;
c) é condicionado a que os pagamentos sejam especificados e comprovados, com indicação do nome, endereço e número de inscrição no Cadastro de Pessoas Físicas ou no Cadastro de Pessoas Jurídicas de quem os recebeu, podendo, na falta de documentação, ser feita indicação do cheque nominativo pelo qual foi efetuado o pagamento.
§ 2° Não se incluem entre as deduções de que trata o inciso I deste artigo as despesas ressarcidas por entidade de qualquer espécie.
§ 3° A soma das deduções previstas nos incisos II e III está limitada a dez por cento da base de cálculo do imposto, na declaração de ajuste anual.
§ 4° As deduções de que trata este artigo serão convertidas em quantidade de Ufir pelo valor desta no mês do pagamento ou no mês em que tiverem sido consideradas na base de cálculo sujeita à incidência do imposto.
Art. 12. As pessoas físicas deverão apresentar anualmente declaração de ajuste, na qual se determinará o saldo do imposto a pagar ou valor a ser restituído.
§ 1° Os ganhos a que se referem o art. 26 desta lei e o inciso I do art. 18 da Lei n° 8.134, de 1990, serão apurados e tributados em separado, não integrarão a base de cálculo do imposto de renda na declaração de ajuste anual e o imposto pago não poderá ser deduzido na declaração.
§ 2° A declaração de ajuste anual, em modelo aprovado pelo Departamento da Receita Federal, deverá ser apresentada até o último dia útil do mês de abril do ano subseqüente ao da percepção dos rendimentos ou ganhos de capital.
§ 3° Ficam dispensadas da apresentação de declaração:
a) as pessoas físicas cujos rendimentos do trabalho assalariado, no ano-calendário, inclusive Gratificação de Natal ou Gratificação Natalina, conforme o caso, acrescidos dos demais rendimentos recebidos, exceto os não tributados ou tributados exclusivamente na fonte, sejam iguais ou inferiores a treze mil Ufir;
b) os aposentados, inativos e pensionistas da Previdência Social da União, dos Estados, do Distrito Federal e dos Municípios ou dos respectivos tesouros, cujos proventos e pensões no ano-calendário, acrescidos dos demais rendimentos recebidos, exceto os não tributados ou tributados exclusivamente na fonte, sejam iguais ou inferiores a treze mil Ufir;
c) outras pessoas físicas declaradas em ato do Ministro da Economia, Fazenda e Planejamento, cuja qualificação fiscal assegure a preservação dos controles fiscais pela administração tributária.
Art. 13. Para efeito de cálculo do imposto a pagar ou do valor a ser restituído, os rendimentos serão convertidos em quantidade de Ufir pelo valor desta no mês em que forem recebidos pelo beneficiário.
Parágrafo único. A base de cálculo do imposto, na declaração de ajuste anual, será a diferença entre as somas, em quantidade de Ufir:
a) de todos os rendimentos percebidos durante o ano-calendário, exceto os isentos, os não tributáveis e os tributados exclusivamente na fonte; e
b ) das deduções de que trata o art. 11 desta lei.
Art. 14. O resultado da atividade rural será apurado segundo o disposto na Lei n° 8.023, de 12 de abril de 1990, e, quando positivo, integrará a base de cálculo do imposto definida no artigo anterior.
§ 1° O resultado da atividade rural e a base de cálculo do imposto serão expressos em quantidade de Ufir.
§ 2° As receitas, despesas e demais valores, que integram o resultado e a base de cálculo, serão convertidos em Ufir pelo valor desta no mês do efetivo pagamento ou recebimento.
Art. 15. O saldo do imposto a pagar ou o valor a ser restituído na declaração de ajuste anual (art. 12) será determinado com observância das seguintes normas:
I - será calculado o imposto progressivo de acordo com a tabela (art. 16);
II - será deduzido o imposto pago ou retido na fonte, correspondente a rendimentos incluídos na base de cálculo;
III - o montante assim determinado, expresso em quantidade de Ufir, constituirá, se positivo, o saldo do imposto a pagar e, se negativo, o valor a ser restituído.
Art. 16. Para fins do ajuste de que trata o artigo anterior, o imposto de renda progressivo será calculado de acordo com a seguinte tabela:                     (Vide Lei nº 8.848, de 28.1.1994)
Art. 17. O saldo do imposto (art. 15, III) poderá ser pago em até seis quotas iguais, mensais e sucessivas, observado o seguinte:
I - nenhuma quota será inferior a cinqüenta Ufir e o imposto de valor inferior a cem Ufir será pago de uma só vez;
II - a primeira quota ou quota única deverá ser paga no mês de abril do ano subseqüente ao da percepção dos rendimentos;
III - as quotas vencerão no último dia útil de cada mês;
IV - é facultado ao contribuinte antecipar, total ou parcialmente, o pagamento do imposto ou das quotas.
Art. 18. Para cálculo do imposto, os valores da tabela progressiva anual (art. 16) serão divididos proporcionalmente ao número de meses do período abrangido pela tributação, em relação ao ano-calendário, nos casos de declaração apresentada:
I - em nome do espólio, no exercício em que for homologada a partilha ou feita a adjudicação dos bens;
II - pelo contribuinte, residente ou domiciliado no Brasil, que se retirar em caráter definitivo do território nacional.
Art. 19. As pessoas físicas ou jurídicas que efetuarem pagamentos com retenção do imposto de renda na fonte deverão fornecer à pessoa física beneficiária, até o dia 28 de fevereiro, documento comprobatório, em duas vias, com indicação da natureza e do montante do pagamento, das deduções e do imposto de renda retido no ano anterior.
§ 1° Tratando-se de rendimentos pagos por pessoas jurídicas, quando não tenha havido retenção do imposto de renda na fonte, o comprovante deverá ser fornecido no mesmo prazo ao contribuinte que o tenha solicitado até o dia 15 de janeiro do ano subseqüente.
§ 2° No documento de que trata este artigo, o imposto retido na fonte, as deduções e os rendimentos deverão ser informados por seus valores em cruzeiros e em quantidade de Ufir, convertidos segundo o disposto na alínea a do parágrafo único do art. 8°, no § 4° do art. 11 e no art. 13 desta lei.
§ 3° As pessoas físicas ou jurídicas que deixarem de fornecer aos beneficiários, dentro do prazo, ou fornecerem com inexatidão, o documento a que se refere este artigo ficarão sujeitas ao pagamento de multa de trinta e cinco Ufir por documento.
§ 4° À fonte pagadora que prestar informação falsa sobre rendimentos pagos, deduções, ou imposto retido na fonte será aplicada a multa de cento e cinqüenta por cento sobre o valor que for indevidamente utilizável como redução do imposto de renda devido, independentemente de outras penalidades administrativas ou criminais.
§ 5° Na mesma penalidade incorrerá aquele que se beneficiar da informação sabendo ou devendo saber da falsidade.
Art. 20. O rendimento produzido por aplicação financeira de renda fixa iniciada a partir de 1° de janeiro de 1992, auferido por qualquer beneficiário, inclusive pessoa jurídica isenta, sujeita-se à incidência do imposto sobre a renda na fonte às alíquotas seguintes:
I - operação iniciada e encerrada no mesmo dia (day trade): quarenta por cento;                    (Revogado pela Lei nº 8.541, de 1992)
II - demais operações: trinta por cento.
§ 1° O disposto neste artigo aplica-se, inclusive, às operações de financiamento realizadas em bolsa de valores, de mercadorias, de futuros e assemelhadas na forma da legislação em vigor.
§ 2° Fica dispensada a retenção do imposto de renda na fonte em relação à operação iniciada e encerrada no mesmo dia quando o alienante for instituição financeira, sociedade de arrendamento mercantil, sociedade corretora de títulos e valores mobiliários ou sociedade distribuidora de títulos e valores mobiliários.
§ 3° A base de cálculo do imposto é constituída pela diferença positiva entre o valor da alienação, líquido do imposto sobre operações de crédito, câmbio e seguro, e sobre operações relativas a títulos e valores mobiliários (IOF) (art. 18 da Lei n° 8.088, de 31 de outubro de 1990) e o valor da aplicação financeira de renda fixa, atualizado com base na variação acumulada da Ufir diária, desde a data inicial da operação até a da alienação.
§ 4° Serão adicionados ao valor de alienação, para fins de composição da base de cálculo do imposto, os rendimentos periódicos produzidos pelo título ou aplicação, bem como qualquer remuneração adicional aos rendimentos prefixados, pagos ou creditados ao alienante e não submetidos à incidência do imposto de renda na fonte, atualizados com base na variação acumulada da Ufir diária, desde a data do crédito ou pagamento até a da alienação.
§ 5° Para fins da incidência do imposto de renda na fonte, a alienação compreende qualquer forma de transmissão da propriedade, bem como a liquidação, resgate ou repactuação do título ou aplicação.
§ 6º Fica incluída na tabela "D" a que se refere o art. 4º, inciso II, da Lei nº 7.940, de 20 de dezembro de 1989, sujeita à alíquota de até 0,64% (sessenta e quatro centésimos por cento), a operação de registro de emissão de outros valores mobiliários.         (Revogado pela Medida Provisória nº 1.072, de 2021)     Produção de efeitos          (Revogado pela Lei nº 14.317, de 2022)   Produção de efeitos
Art. 21. Nas aplicações de fundo de renda fixa, resgatadas a partir de 1º de janeiro de 1992, a base de cálculo do imposto de renda na fonte será constituída pela diferença positiva entre o valor do resgate, líquido de IOF, e o custo de aquisição da quota, atualizado com base na variação acumulada da Ufir diária, desde a data da conversão da aplicação em quotas até a reconversão das quotas em cruzeiros.
§ 1º Na determinação do custo de aquisição da quota, quando atribuída a remuneração ao valor resgatado, observar-se-á a precedência segundo a ordem seqüencial direta das aplicações realizadas pelo beneficiário.
§ 2º Os rendimentos auferidos pelos fundos de renda fixa e as alienações de títulos ou aplicações por eles realizadas ficam excluídos respectivamente, da incidência do imposto de renda na fonte e do IOF.                  (Vide Lei nº 8.894, de 21/06/94)
§ 3º O imposto de renda na fonte, calculado à alíquota de trinta por cento, e o IOF serão retidos pelo administrador do fundo de renda fixa na data do resgate.
§ 4º Excluem-se do disposto neste artigo as aplicações em Fundo de Aplicação Financeira (FAF), que continuam sujeitas à tributação pelo imposto de renda na fonte à alíquota de cinco por cento sobre o rendimento bruto apropriado diariamente ao quotista.
§ 5º Na determinação da base de cálculo do imposto em relação ao resgate de quota existente em 31 de dezembro de 1991, adotar-se-á, a título de custo de aquisição, o valor da quota da mesma data.
Art. 22. São isentos do imposto de renda na fonte:
I - os rendimentos creditados ao quotista pelo Fundo de Investimento em Quotas de Fundos de Aplicação, correspondente aos créditos apropriados por FAF;
II - os rendimentos auferidos por FAF, tributados quando da apropriação ao quotista.
Art. 23. A operação de mútuo e a operação de compra vinculada à revenda, no mercado secundário, tendo por objeto ouro, ativo financeiro, iniciadas a partir de 1° de janeiro de 1992, ficam equiparadas à operação de renda fixa para fins de incidência do imposto de renda na fonte.
§ 1° Constitui fato gerador do imposto a liquidação da operação de mútuo ou a revenda de ouro, ativo financeiro.
§ 2° A base de cálculo do imposto nas operações de mútuo será constituída:
a) pelo valor do rendimento em moeda corrente, atualizado entre a data do recebimento e a data de liquidação do contrato; ou
b) quando o rendimento for fixado em quantidade de ouro, pelo valor da conversão do ouro em moeda corrente, estabelecido com base nos preços médios das operações realizadas no mercado à vista da bolsa em que ocorrer o maior volume de ouro transacionado na data de liquidação do contrato.
§ 3° A base de cálculo nas operações de revenda e de compra de ouro, quando vinculadas, será constituída pela diferença positiva entre o valor de revenda e o de compra do ouro, atualizada com base na variação acumulada da Ufir diária, entre a data de início e de encerramento da operação.
§ 4° O valor da operação de que trata a alínea a do § 2° será atualizado com base na Ufir diária.
§ 5° O imposto de renda na fonte será calculado aplicando-se alíquotas previstas no art. 20, de acordo com o prazo de operação.
§ 6° Fica o Poder Executivo autorizado a baixar normas com vistas a definir as características da operação de compra vinculada à revenda, bem como a equiparar às operações de que trata este artigo outras que, pelas suas características produzam os mesmos efeitos das operações indicadas.
§ 7° O Conselho Monetário Nacional poderá estabelecer prazo mínimo para as operações de que trata este artigo.
Art. 24. Fica dispensada a retenção do imposto de renda na fonte de que tratam os arts. 20, 21 e 23, sobre rendimentos produzidos por aplicações financeiras de renda fixa, quando o beneficiário for pessoa jurídica tributada com base no lucro real, desde que atendidas, cumulativamente, as seguintes condições em relação à operação:                     (Revogado pela Lei nº 8.541, de 1992)
I - tenha por objeto a aquisição de título ou realização de aplicação exclusivamente sob a forma nominativa, intransferível por endosso;                     (Revogado pela Lei nº 8.541, de 1992)
II - o pagamento ou resgate seja efetuado por cheque cruzado nominativo, não endossável, para depósito em conta do beneficiário ou mediante crédito em conta corrente por ele mantida junto à entidade, dentre as nomeadas no art. 20, § 2°;                    (Revogado pela Lei nº 8.541, de 1992)
III - seja apresentada, no ato da cessão ou liquidação, a nota de negociação relativa à aquisição do título ou à realização da aplicação;                     (Revogado pela Lei nº 8.541, de 1992)
IV - seja comprovado à fonte pagadora, por escrito, pelo beneficiário, o enquadramento no disposto no caput deste artigo ou a condição de entidade imune.                (Revogado pela Lei nº 8.541, de 1992)
Parágrafo único. A dispensa de que trata este artigo não se aplica em relação aos rendimentos auferidos nas operações:(Revogado pela Lei nº 8.541, de 1992)
a) iniciadas e encerradas no mesmo dia, exceto no caso previsto no art. 20, § 2°;                    (Revogado pela Lei nº 8.541, de 1992)
b) de mútuo, realizadas entre pessoas jurídicas não ligadas, exceto se, pelo menos uma das partes, for qualquer das pessoas jurídicas mencionadas no art. 20, § 2°;                  (Revogado pela Lei nº 8.541, de 1992)
c) de que trata o § 4° do art. 21.                      (Revogado pela Lei nº 8.541, de 1992)
Art. 25. O rendimento auferido no resgate, a partir de 1° de janeiro de 1992, de quota de fundo mútuo de ações, clube de investimento e outros fundos da espécie, inclusive Plano de Poupança e Investimentos (PAIT), de que trata o Decreto-Lei n° 2.292, de 21 de novembro de 1986, constituídos segundo a legislação aplicável, quando o beneficiário for pessoa física ou pessoa jurídica não tributada com base no lucro real, inclusive isenta, sujeita-se à incidência do imposto de renda na fonte à alíquota de vinte e cinco por cento.
§ 1° A base de cálculo do imposto é constituída pela diferença positiva entre o valor de resgate e o custo médio de aquisição da quota, atualizado com base na variação acumulada da Ufir diária da data da conversão em quotas até a de reconversão das quotas em cruzeiros.
§ 2° Os ganhos líquidos a que se refere o artigo seguinte e os rendimentos produzidos por aplicações financeiras de renda fixa, auferidos por fundo mútuo de ações, clube de investimentos e outros fundos da espécie, não estão sujeitos à incidência do imposto de renda na fonte.
§ 3° O imposto será retido pelo administrador do fundo ou clube de investimento na data do resgate.
§ 4° Fica o Poder Executivo autorizado a permitir a compensação de perdas ocorridas em aplicações de que trata este artigo.
Art. 26. Ficam sujeitas ao pagamento do imposto de renda, à alíquota de vinte e cinco por cento, a pessoa física e a pessoa jurídica não tributada com base no lucro real, inclusive isenta, que auferirem ganhos líquidos nas operações realizadas nas bolsas de valores, de mercadorias, de futuros e assemelhadas, encerradas a partir de 1° de janeiro de 1992.
§ 1° Os custos de aquisição, os preços de exercício e os prêmios serão considerados pelos valores médios pagos, atualizados com base na variação acumulada da Ufir diária da data da aquisição até a data da alienação do ativo.
§ 2° O Poder Executivo poderá baixar normas para apuração e demonstração dos ganhos líquidos, bem como autorizar a compensação de perdas em um mesmo ou entre dois ou mais mercados ou modalidades operacionais, previstos neste artigo, ressalvado o disposto no art. 28 desta lei.
§ 3° O disposto neste artigo aplica-se, também, aos ganhos líquidos decorrentes da alienação de ouro, ativo financeiro, fora da bolsa, com a interveniência de instituições integrantes do Sistema Financeiro Nacional.
§ 4° O imposto de que trata este artigo será apurado mensalmente.
Art. 27. As deduções de despesas, bem como a compensação de perdas na forma prevista no § 2° do artigo precedente, são admitidas exclusivamente para as operações realizadas nos mercados organizados, geridos ou sob responsabilidade de instituição credenciada pelo Poder Executivo e com objetivos semelhantes ao das bolsas de valores, de mercadorias ou de futuros.
Art. 28. Os prejuízos decorrentes de operações financeiras de compra e subseqüente venda ou de venda e subseqüente compra, realizadas no mesmo dia (day-trade), tendo por objeto ativo, título, valor mobiliário ou direito de natureza e características semelhantes, somente podem ser compensados com ganhos auferidos em operações da mesma espécie ou em operações de cobertura (hedge) à qual estejam vinculadas nos termos admitidos pelo Poder Executivo.
§ 1° O ganho líquido mensal corresponde às operações day-trade, quando auferido por beneficiário dentre os referidos no art. 26, integra a base de cálculo do imposto de renda de que trata o mesmo artigo.
§ 2° Os prejuízos decorrentes de operações realizadas fora de mercados organizados, geridos ou sob responsabilidade de instituição credenciada pelo Poder Público, não podem ser deduzidos da base de cálculo do imposto de renda e da apuração do ganho líquido de que trata o art. 26, bem como não podem ser compensados com ganhos auferidos em operações de espécie, realizadas em qualquer mercado.
Art. 29. Os beneficiários residentes ou domiciliados no exterior sujeitam-se, a partir de 1° de janeiro de 1992, às mesmas normas de tributação pelo imposto de renda, previstas para os beneficiários residentes ou domiciliadas no País, em relação:
I - aos rendimentos decorrentes de aplicações financeiras de renda fixa;
II - aos ganhos líquidos auferidos em operações realizadas em bolsas de valores, de mercadorias, de futuros e assemelhadas;
III - aos rendimentos obtidos em aplicações em fundos de investimento e clubes de ações.
Art. 29. Os residentes ou domiciliados no exterior sujeitam-se às mesmas normas de tributação pelo imposto de renda, previstas para os residentes ou domiciliados no País, em relação aos:                  (Redação dada pela Lei nº 8.849, de 1994)
I - rendimentos decorrentes de aplicações financeiras de renda fixa;
II - ganhos líquidos auferidos em operações realizadas em bolsas de valores, de mercadorias, de futuros e assemelhadas;
III - rendimentos obtidos em aplicações em fundos e clubes de investimentos de renda variável.
"""

# Função para extrair artigos, parágrafos e incisos
def extrair_estrutura(texto):
    estrutura = []
    artigos = re.split(r'\nArt\. \d+º', texto)
    titulo = artigos.pop(0).strip()
    
    for i, artigo in enumerate(artigos, start=1):
        artigo_dict = {
            'artigo': f'Art. {i}º',
            'texto': artigo.split('§')[0].strip(),
            'paragrafos': []
        }
        
        paragrafos = re.split(r'\n§ \d+º', artigo)
        if len(paragrafos) > 1:
            paragrafos.pop(0)  # Remove o texto antes do primeiro parágrafo
        
        for j, paragrafo in enumerate(paragrafos, start=1):
            paragrafo_dict = {
                'paragrafo': f'§ {j}º',
                'texto': paragrafo.strip(),
                'incisos': []
            }
            
            incisos = re.split(r'\n[IVX]+\s-\s', paragrafo)
            if len(incisos) > 1:
                incisos.pop(0)  # Remove o texto antes do primeiro inciso
            
            for inciso in incisos:
                paragrafo_dict['incisos'].append(inciso.strip())
            
            artigo_dict['paragrafos'].append(paragrafo_dict)
        
        estrutura.append(artigo_dict)
    
    return {
        'titulo': titulo,
        'artigos': estrutura
    }

# Extrair a estrutura da lei
estrutura_lei = extrair_estrutura(texto_lei)

# Converter para JSON
lei_json = json.dumps(estrutura_lei, indent=4, ensure_ascii=False)

# Salvar o JSON em um arquivo
with open('lei.json', 'w', encoding='utf-8') as file:
    file.write(lei_json)

# Exibir o JSON gerado
print(lei_json)
