import unittest

import PyNFSe.nfse.Curitiba.serializacao as s
from PyNFSe.tests.Curitiba.basetestesserializacao import BaseTestesSerializacao, xml_expected


class SerializacaoComunicacaoTestCase(BaseTestesSerializacao):

    def test_consultar_nfse_por_nota(self):
        numero_nota = 179
        xml_consultar_nfse = s.consulta_nfse(self.prestador, numero_nota)

        xml_consultar_nfse_expected = xml_expected('ConsultarNfseEnvio-por_nota.xml')

        self.assertEqual(xml_consultar_nfse, xml_consultar_nfse_expected)

    def test_envio_lote_rps(self):
        xml_lote_rps = s.envio_lote_rps(self.lote_rps)

        xml_lote_rps_expected = xml_expected('EnviarLoteRpsEnvio.xml')

        self.assertEqual(xml_lote_rps, xml_lote_rps_expected)

    def test_consultar_lote_rps(self):
        xml_consultar_lote = s.consultar_situacao_lote_rps(self.prestador, '636174090357960929')

        xml_consultar_lote_expected = xml_expected('ConsultarSituacaoLoteRpsEnvio.xml')

        self.assertEqual(xml_consultar_lote, xml_consultar_lote_expected)

if __name__ == '__main__':
    unittest.main()