import './styles.css'


export function SuccessComponent () {
    return (
         <div className="success-container">
        <div className="success-card">
            <div className="success-icon">
                <i className="fas fa-check-circle"></i>
            </div>

            <h1>Оплата прошла успешно!</h1>
            <p className="thank-you">Спасибо! Ваш заказ оформлен и передан в обработку.</p>

        </div>
    </div>
    )
}