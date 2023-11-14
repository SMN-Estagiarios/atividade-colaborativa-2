const cadastrar_livro = (titulo, autor, isbn) => {
  const book = {
    id: titulo + autor,
    author: autor,
    register: isbn,
  };

  return book;
};
