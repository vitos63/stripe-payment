

const API_BASE_URL: string = process.env.REACT_APP_API_URL ?? 'http://localhost:8000'


export async function getAllProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}/get-all-products/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    )
    const data = await response.json()
    return data}
    catch (error) {
        console.error("Ошибка при получении товаров")
        throw error
    }
}


export async function fetchBuyProduct(productId: number) {
    try {
        const response = await fetch(`${API_BASE_URL}/checkout/`, {
            method: 'POST',
            body: JSON.stringify({ product_id: productId }),
            headers: {
                'Content-Type': 'application/json',
            },
        }
    )
    const data = await response.json();
    return data.url
}
    catch (error) {
        console.error("Ошибка при получении товаров")
        throw error
    }
}