import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import { ProductComponent } from './components/ProductsComponent';
import { SuccessComponent } from './components/SuccessComponent';

export default function App() {
  return (
    <div className="App">
      <Router>
      <Routes>
     <Route path='/' element={<ProductComponent/>}></Route>
     <Route path='/success/' element={<SuccessComponent/>}></Route>
     </Routes>
     </Router>
    </div>
  );
}
