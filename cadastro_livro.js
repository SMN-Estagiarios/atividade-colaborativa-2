const cadastrar_livro = (titulo, autor, isbn) => {
  const book = {
    id: isbn + titulo,
    author: autor,
    register: isbn,
  };
  console.log(book);

  return book;
};

const cadastro_geral = () => {
  cadastrar_livro("Colheita maldita", "Stephen King", "2587964");
};

cadastro_geral();
