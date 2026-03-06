import { useEffect, useState } from "react"
import { getAllProducts, fetchBuyProduct } from "../api/api"
import { Product } from "../interfaces/ProductInterface"
import "./styles.css";


export function ProductComponent () {
    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        const fetchProducts = async () => {
        setProducts(await getAllProducts())
    }
    fetchProducts()
    }, []
    )
    async function buyProduct(productId: number){
        const url = await fetchBuyProduct(productId)
        window.location.href = url;
    }
 return (
    <div className="container">
      <h2 className="title">Наши товары</h2>
      <ul className="productList">
        {products.map((product) => (
          <li key={product.id} className="productCard">
            <div className="productInfo">
              <span className="productTitle">{product.title}</span>
              <span className="productPrice">{product.price} USD</span>
            </div>
            <button
              className="buyButton"
              onClick={() => buyProduct(product.id)}
            >
              Купить
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}