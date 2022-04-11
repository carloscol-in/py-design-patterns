from random import randint


class Generator:
  def generate(self, count):
    return [randint(1, 9) for x in range(count)]


class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result


class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True


class MagicSquareGenerator:
  def generate(self, size):
    # todo - return a magic square of the given size
    generator = Generator()
    matrix = [generator.generate(size) for i in range(size)]
    splitter = Splitter()
    verifier = Verifier()
    splitted_matrix = splitter.split(matrix)
    counter = 0

    while not verifier.verify(splitted_matrix):
        # if counter % 100 == 0:
        #     response = input('Keep going? Y/n').lower().strip() in ['y', '']
        #     if not response:
        #         break
        matrix = [generator.generate(size) for i in range(size)]
        splitted_matrix = splitter.split(matrix)
        counter += 1

    return splitted_matrix

if __name__ == '__main__':
    magic = MagicSquareGenerator()
    print(magic.generate(2))