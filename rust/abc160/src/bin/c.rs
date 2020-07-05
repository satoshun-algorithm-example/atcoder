fn main() {
    let (k, _n) = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s = s.trim_end().to_owned();

        let mut ws = s.split_whitespace();
        let n: i32 = ws.next().unwrap().parse().unwrap();
        let m: i32 = ws.next().unwrap().parse().unwrap();
        (n, m)
    };

    let a_s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().to_owned()
    };
    let whitespace = a_s.split_whitespace();
    let b: Vec<i32> = whitespace.into_iter().map(|x| x.parse::<i32>().unwrap()).collect();

    let mut max = *b.get(0).unwrap() + (k - *b.get(b.len() - 1).unwrap());
    for i in 0..(b.len() - 1) {
        let a1 = b.get(i).unwrap();
        let a2 = b.get(i + 1).unwrap();
        max = std::cmp::max(max, a2 - a1);
    }

    println!("{}", k - max);
}
