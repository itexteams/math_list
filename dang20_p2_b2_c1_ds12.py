import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang20_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            R_val = randint(4, 10)
            R_str = str(R_val)
            D_str = str(2 * R_val)
            R2_str = str(R_val**2)

            def fmt_num(val):
                if val == int(val):
                    return str(int(val))
                return str(round(val, 2)).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Từ một tấm bạt hình tròn có bán kính $%s$ mét, người ta cắt bỏ $4$ phần (như hình vẽ) để giữ lại một phần gồm: Một hình vuông cạnh bằng $x$ (mét) và $4$ tam giác cân tại các đỉnh nằm trên đường tròn. Sau đó, người ta gấp $4$ tam giác này lên để chụm đầu lại tạo thành một cái lều có dạng hình chóp tứ giác đều.
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8]
                \\def\\R{2.5}
                \\def\\x{0.8}
                \\fill[cyan!20] (-\\x,-\\x) rectangle (\\x,\\x);
                \\fill[orange!30] (-\\x,\\x) -- (0,\\R) -- (\\x,\\x) -- cycle;
                \\fill[orange!30] (\\x,\\x) -- (\\R,0) -- (\\x,-\\x) -- cycle;
                \\fill[orange!30] (\\x,-\\x) -- (0,-\\R) -- (-\\x,-\\x) -- cycle;
                \\fill[orange!30] (-\\x,-\\x) -- (-\\R,0) -- (-\\x,\\x) -- cycle;
                \\draw[blue, thick] (0,0) circle (\\R);
                \\draw[blue, thick] (-\\x,-\\x) rectangle (\\x,\\x);
                \\draw[red, thick] (-\\x,\\x) -- (0,\\R) -- (\\x,\\x);
                \\draw[red, thick] (\\x,\\x) -- (\\R,0) -- (\\x,-\\x);
                \\draw[red, thick] (\\x,-\\x) -- (0,-\\R) -- (-\\x,-\\x);
                \\draw[red, thick] (-\\x,-\\x) -- (-\\R,0) -- (-\\x,\\x);
                \\fill (0,\\R) circle (1.5pt);
                \\fill (\\R,0) circle (1.5pt);
                \\fill (0,-\\R) circle (1.5pt);
                \\fill (-\\R,0) circle (1.5pt);
                \\fill (-\\x,\\x) circle (1.5pt);
                \\fill (\\x,\\x) circle (1.5pt);
                \\fill (\\x,-\\x) circle (1.5pt);
                \\fill (-\\x,-\\x) circle (1.5pt);
            \\end{tikzpicture}
            \\hspace{1cm}
            \\begin{tikzpicture}[scale=0.8]
                \\def\\dx{1.5} \\def\\dy{1.5} \\def\\wx{4}
                \\coordinate (N) at (0,0);
                \\coordinate (P) at (\\wx,0);
                \\coordinate (Q) at (\\wx+\\dx,\\dy);
                \\coordinate (M) at (\\dx,\\dy);
                \\coordinate (S) at (\\wx/2+\\dx/2, 4.5);
                \\fill[cyan!20] (M) -- (N) -- (P) -- (Q) -- cycle;
                \\draw[red, dashed, thick] (M) -- (N);
                \\draw[red, dashed, thick] (M) -- (Q);
                \\draw[red, dashed, thick] (S) -- (M);
                \\draw[red, thick] (N) -- (P) -- (Q);
                \\draw[red, thick] (S) -- (N);
                \\draw[red, thick] (S) -- (P);
                \\draw[red, thick] (S) -- (Q);
                \\fill (S) circle (1.5pt);
                \\fill (M) circle (1.5pt);
                \\fill (N) circle (1.5pt);
                \\fill (P) circle (1.5pt);
                \\fill (Q) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (R_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Điều kiện xác định của $x$ là $0 < x < %s$' % R_str
            nb_da_1_s = 'Điều kiện xác định của $x$ là $0 < x < %s$' % sp.latex(sp.Rational(R_val, 2) * sp.sqrt(2))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.6]
                \\def\\R{2.5}
                \\def\\x{0.8}
                \\fill[cyan!20] (-\\x,-\\x) rectangle (\\x,\\x);
                \\fill[orange!30] (-\\x,\\x) -- (0,\\R) -- (\\x,\\x) -- cycle;
                \\fill[orange!30] (\\x,\\x) -- (\\R,0) -- (\\x,-\\x) -- cycle;
                \\fill[orange!30] (\\x,-\\x) -- (0,-\\R) -- (-\\x,-\\x) -- cycle;
                \\fill[orange!30] (-\\x,-\\x) -- (-\\R,0) -- (-\\x,\\x) -- cycle;
                \\draw[blue, thick] (0,0) circle (\\R);
                \\draw[red, thick] (-\\x,\\x) -- (0,\\R) -- (\\x,\\x);
                \\draw[red, thick] (\\x,\\x) -- (\\R,0) -- (\\x,-\\x);
                \\draw[red, thick] (\\x,-\\x) -- (0,-\\R) -- (-\\x,-\\x);
                \\draw[red, thick] (-\\x,-\\x) -- (-\\R,0) -- (-\\x,\\x);
                \\draw[dashed, thick] (-\\x,-\\x) rectangle (\\x,\\x);
                \\draw[dashed, thick] (-\\R,0) -- (\\R,0);
                \\draw[dashed, thick] (0,-\\R) -- (0,\\R);
                \\fill (0,\\R) circle (1.5pt) node[above] {$A$};
                \\fill (\\R,0) circle (1.5pt) node[right] {$B$};
                \\fill (0,-\\R) circle (1.5pt) node[below] {$C$};
                \\fill (-\\R,0) circle (1.5pt) node[left] {$D$};
                \\fill (-\\x,\\x) circle (1.5pt) node[above left] {$M$};
                \\fill (\\x,\\x) circle (1.5pt) node[above right] {$Q$};
                \\fill (\\x,-\\x) circle (1.5pt) node[below right] {$P$};
                \\fill (-\\x,-\\x) circle (1.5pt) node[below left] {$N$};
                \\fill (0,0) circle (1.5pt) node[above right] {$O$};
                \\fill (-\\x,0) circle (1.5pt) node[above left] {$K$};
                \\fill (\\x,0) circle (1.5pt) node[above right] {$T$};
                \\node at (0, -3.5) {\\textit{Hình 1}};
            \\end{tikzpicture}
            \\hspace{1cm}
            \\begin{tikzpicture}[scale=0.6]
                \\def\\dx{1.5} \\def\\dy{1.5} \\def\\wx{4}
                \\coordinate (N) at (0,0);
                \\coordinate (P) at (\\wx,0);
                \\coordinate (Q) at (\\wx+\\dx,\\dy);
                \\coordinate (M) at (\\dx,\\dy);
                \\coordinate (O) at (\\wx/2+\\dx/2,\\dy/2);
                \\coordinate (S) at (\\wx/2+\\dx/2, 4.5);
                \\coordinate (K) at (\\dx/2, \\dy/2);
                \\coordinate (T) at (\\wx+\\dx/2, \\dy/2);
                \\fill[cyan!20] (M) -- (N) -- (P) -- (Q) -- cycle;
                \\draw[red, dashed, thick] (M) -- (N);
                \\draw[red, dashed, thick] (M) -- (Q);
                \\draw[dashed, thick] (S) -- (M);
                \\draw[dashed, thick] (K) -- (T);
                \\draw[dashed, thick] (S) -- (O);
                \\draw[dashed, thick] (S) -- (K);
                \\draw[red, thick] (N) -- (P) -- (Q);
                \\draw[red, thick] (S) -- (N);
                \\draw[red, thick] (S) -- (P);
                \\draw[red, thick] (S) -- (Q);
                \\draw[thick] (S) -- (T);
                \\fill (S) circle (1.5pt) node[above] {$S$};
                \\fill (M) circle (1.5pt) node[left] {$M$};
                \\fill (N) circle (1.5pt) node[left] {$N$};
                \\fill (P) circle (1.5pt) node[right] {$P$};
                \\fill (Q) circle (1.5pt) node[right] {$Q$};
                \\fill (O) circle (1.5pt) node[below] {$O$};
                \\fill (K) circle (1.5pt) node[below] {$K$};
                \\fill (T) circle (1.5pt) node[below right] {$T$};
                \\node at (\\wx/2+\\dx/2, -1.5) {\\textit{Hình 2}};
            \\end{tikzpicture}
            \\end{center}
            Đặt $DK = TB = a$ và $MN = NP = PQ = QM = x$ khi đó: $a + x + a = %s \\Rightarrow 2a = %s - x$.\\\\
            Mặt khác: $2a > x \\Leftrightarrow %s - x > x \\Leftrightarrow 0 < x < %s$.''' % (D_str, D_str, D_str, R_str))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Diện tích vải xung quanh của lều được tính bằng $S_{xq} = %sx$' % D_str
            th_da_1_s = 'Diện tích vải xung quanh của lều được tính bằng $S_{xq} = %sx - x^2$' % D_str
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Diện tích hình vuông cạnh $x$: $S_{HV} = x^2$.\\\\
            Diện tích tam giác có cạnh đáy là $x$ và chiều cao là $a$: $S_{\\Delta} = \\frac{1}{2}\\cdot a \\cdot x$.\\\\
            Diện tích vải xung quanh của lều là:\\\\
            $S_{xq} = S_{HV} + 4\\cdot S_{\\Delta} = x^2 + 4\\cdot \\frac{1}{2}\\cdot a \\cdot x = x(x+2a) = x^2 + x(%s - x) = %sx$.''' % (D_str, D_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Thể tích của không gian bên trong lều tính là $V(x) = \\frac{x^2}{3}\\sqrt{%s - %sx}$' % (R2_str, R_str)
            vd_da_1_s = 'Thể tích của không gian bên trong lều tính là $V(x) = \\frac{x^2}{3}\\sqrt{%s - %sx}$' % (R2_str, D_str)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét hình 2 ta có, chiều cao của lều:\\\\ $SO = \\sqrt{SK^2 - OK^2} = \\sqrt{a^2 - \\left(\\frac{x}{2}\\right)^2} = \\sqrt{\\left(\\frac{%s - x}{2}\\right)^2 - \\left(\\frac{x}{2}\\right)^2}$.\\\\
            Thể tích lều là:\\\\ $V(x) = \\frac{1}{3}x^2\\sqrt{\\left(\\frac{%s - x}{2}\\right)^2 - \\left(\\frac{x}{2}\\right)^2} = \\frac{1}{3}x^2\\sqrt{%s - %sx + \\frac{x^2}{4} - \\frac{x^2}{4}} = \\frac{x^2}{3}\\sqrt{%s - %sx}$.''' % (D_str, D_str, R2_str, R_str, R2_str, R_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Khi thể tích của lều đạt giá trị lớn nhất thì $\\tan$ của góc tạo bởi mặt bên và mặt đáy bằng $\\frac{\\sqrt{5}}{2}$'
            vdc_da_1_s = 'Khi thể tích của lều đạt giá trị lớn nhất thì $\\tan$ của góc tạo bởi mặt bên và mặt đáy bằng $\\frac{\\sqrt{3}}{2}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Tính toán các số cho lời giải
            x_max_frac = sp.Rational(4*R_val, 5)
            if x_max_frac.q == 1:
                x_max_frac_str = str(x_max_frac.p)
            else:
                x_max_frac_str = f"\\frac{{{x_max_frac.p}}}{{{x_max_frac.q}}}"

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Thể tích: $V(x) = \\frac{x^2}{3}\\sqrt{%s - %sx} \\Rightarrow V'(x) = \\frac{%s x(%s - 5x)}{6\\sqrt{%s - %sx}} = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = 0 \\, (\\text{loại}) \\\\ x = %s \\, (\\text{nhận}) \\end{array} \\right.$.\\\\
            Bảng biến thiên:\\\\
            \\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=3,lgt=1.5]
            {$x$/1,$V'(x)$/0.7,$V(x)$/2}
            {0,$%s$,$%s$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/ ,+/$V(\\max)$,-/ }
            \\end{tikzpicture}
            \\end{center}
            Khi đó: $x = %s \\Rightarrow \\left\\{ \\begin{array}{l} SK = ST = %s \\\\ SO = %s \\\\ OK = OT = %s \\end{array} \\right. \\Rightarrow \\tan \\alpha = \\tan \\widehat{STO} = \\frac{SO}{OT} = \\frac{\\sqrt{5}}{2}$.''' % (
            R2_str, R_str,
            R_str, str(4*R_val), R2_str, R_str,
            x_max_frac_str,
            x_max_frac_str, R_str,
            fmt_num(0.8*R_val),
            fmt_num(0.6*R_val),
            sp.latex(sp.Rational(R_val, 5)*sp.sqrt(5)),
            fmt_num(0.4*R_val)
            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

