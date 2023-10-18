const Tshape = [
    [0, 1, 0],
    [1, 1, 1],
];

const Lshape = [
    [1, 0],
    [1, 0],
    [1, 1],
];

const Ishape = [[1], [1], [1]];

const SquareShape = [
    [1, 1],
    [1, 1],
];

function initGrid(rows, cols) {
    return Array.from({ length: rows }, () => Array(cols).fill(0));
}

function randomPiece() {
    const shapes = [Tshape, Lshape, Ishape, SquareShape];
    const randomIndex = Math.floor(Math.random() * shapes.length);

    return shapes[randomIndex];
}

function rotatePieceLeft(piece) {
    const rows = piece.length;
    const cols = piece[0].length;

    let newArray = Array.from({ length: cols }, () => Array(rows).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            newArray[j][i] = piece[i][j];
        }
    }

    return newArray;
}

function rotatePieceRight(piece) {
    const rows = piece.length;
    const cols = piece[0].length;

    let newArray = Array.from({ length: cols }, () => Array(rows).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            newArray[j][i] = piece[rows - i - 1][cols - j - 1]; // -1 to account for 0 indexing
        }
    }

    return newArray;
}

function createNewPiece(grid) {
    const piece = randomPiece();
    const xpos = Math.round((grid.length - piece.length) / 2);
    for (let i = 0; i < piece.length; i++) {
        for (let j = 0; j < piece[0].length; j++) {
            // end game if grid section is already 0
            if (grid[i + xpos][j] === 1) {
                return false;
            }

            grid[i + xpos][j] = piece[i][j];
        }
    }
    return grid;
}

function main() {
    let grid = initGrid(15, 10);

    grid = createNewPiece(grid);
}

piece = randomPiece();
console.log(piece);
console.log(rotatePieceRight(piece));
