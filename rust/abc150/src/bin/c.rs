use itertools::Itertools;

macro_rules! input {
    (source = $s:expr, $($r:tt)*) => {
        let mut iter = $s.split_whitespace();
        input_inner!{iter, $($r)*}
    };
    ($($r:tt)*) => {
        let s = {
            use std::io::Read;
            let mut s = String::new();
            std::io::stdin().read_to_string(&mut s).unwrap();
            s
        };
        let mut iter = s.split_whitespace();
        input_inner!{iter, $($r)*}
    };
}

macro_rules! input_inner {
    ($iter:expr) => {};
    ($iter:expr, ) => {};

    ($iter:expr, $var:ident : $t:tt $($r:tt)*) => {
        let $var = read_value!($iter, $t);
        input_inner!{$iter $($r)*}
    };
}

macro_rules! read_value {
    ($iter:expr, ( $($t:tt),* )) => {
        ( $(read_value!($iter, $t)),* )
    };

    ($iter:expr, [ $t:tt ; $len:expr ]) => {
        (0..$len).map(|_| read_value!($iter, $t)).collect::<Vec<_>>()
    };

    ($iter:expr, chars) => {
        read_value!($iter, String).chars().collect::<Vec<char>>()
    };

    ($iter:expr, usize1) => {
        read_value!($iter, usize) - 1
    };

    ($iter:expr, $t:ty) => {
        $iter.next().unwrap().parse::<$t>().expect("Parse error")
    };
}

fn main() {
    input! {
        n: usize,
        ps: [usize; n],
        qs: [usize; n],
    }

    let perms = (1..n + 1).permutations(n);

    let mut s1i = 0;
    for item in perms {
        let mut flag = false;
        for (index, value) in item.iter().enumerate() {
            let a = ps[index];
            let v = *value as usize;
            if a != v {
                flag = true;
                break;
            }
        }

        s1i += 1;
        if !flag {
            break;
        }
    }

    let mut s2i = 0;
    for item in (1..n + 1).permutations(n) {
        let mut flag = false;
        for (index, value) in item.iter().enumerate() {
            let a = qs[index];
            let v = *value as usize;
            if a != v {
                flag = true;
                break;
            }
        }

        s2i += 1;
        if !flag {
            break;
        }
    }

    println!("{}", ((s1i - s2i) as i32).abs());
}
