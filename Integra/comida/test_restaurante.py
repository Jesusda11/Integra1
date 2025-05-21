import unittest
from unittest.mock import MagicMock
from menu import Plato  # Asegúrate de usar el nombre real del archivo
from restaurante import Restaurante
class TestRestaurante(unittest.TestCase):
    def test_agregar_plato_a_pedido(self):
        plato = Plato("Hamburguesa", 15.0)

        menu_mock = MagicMock()
        menu_mock.obtener_plato.return_value = plato

        pedido_mock = MagicMock()

        restaurante = Restaurante(menu_mock)

        resultado = restaurante.agregar_plato_a_pedido(pedido_mock, "Hamburguesa")

         #Verficar que al menu si le llamamos el metodo obtener plato.
        menu_mock.obtener_plato.assert_called_once_with("Hamburguesa")

        pedido_mock.agregar_plato.assert_called_once_with(plato)

        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()
