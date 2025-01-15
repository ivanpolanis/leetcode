package leetcode

import "testing"

func Test_evalRPN(t *testing.T) {
	type args struct {
		tokens []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test 1",
			args: args{
				tokens: []string{"2", "1", "+", "3", "*"},
			},
			want: 9,
		},

		{
			name: "test 2",
			args: args{
				tokens: []string{"4", "13", "5", "/", "+"},
			},
			want: 6,
		},
	}
	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := evalRPN(tt.args.tokens); got != tt.want {
				t.Errorf("evalRPN() = %v, want %v", got, tt.want)
			}
		})
	}
}
