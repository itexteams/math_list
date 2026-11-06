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


def bt_dang44_p2_b2_c1_ds12(self):
    # Khai báo biến
    t = symbols('t')

    # Sinh thông số ngẫu nhiên cho bài toán
    m = random.randint(1, 3)       # Hệ số biến thiên
    y1 = random.randint(1, 3)      # Tốc độ ban đầu tại t = 0
    y2 = y1 + m                    # Tốc độ cực đại tại t = 1

    # Các hệ số đa thức f(t) = a*t^3 + b*t^2 + c*t + d
    a_val = -2 * m
    b_val = 3 * m
    c_val = 0
    d_val = y1

    f_expr = a_val * t**3 + b_val * t**2 + d_val
    f_prime = diff(f_expr, t)

    wrong_f_expr = -m * t**3 + 3 * m * t**2 + y1
    val_1_5 = y1
    val_1_5_str = str(val_1_5)
    wrong_val_1_5 = y2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một công ty khởi nghiệp mô hình hóa tốc độ tăng trưởng doanh thu hàng năm $y = f(t)$ (đơn vị: tỷ đồng/năm) theo thời gian $t$ (đơn vị: năm, với $t \\ge 0$) bằng một hàm số đa thức bậc ba $y = a t^3 + b t^2 + c t + d$ ($a \\neq 0$) có đồ thị như hình vẽ.
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[->, line width=1pt] (-0.8,0) -- (2.5,0) node[below] {$t$};
        \\draw[->, line width=1pt] (0,-0.8) -- (0,%s) node[left] {$y$};
        \\draw (0,0) node[below left] {$O$};
        \\draw[line width=1pt, domain=-0.45:1.75, samples=100] plot (\\x, {%s*(\\x)^3 + %s*(\\x)^2 + %s});
        \\draw[line width=1pt, dashed] (1,0) node[below] {$1$} -- (1,%s) -- (0,%s) node[left] {$%s$};
        \\draw (0,%s) node[left] {$%s$};
        \\draw (2,0) node[below] {$2$};
        \\fill (0,%s) circle (1pt);
        \\fill (1,%s) circle (1pt);
        \\fill (1,0) circle (1pt);
        \\fill (2,0) circle (1pt);
    \\end{tikzpicture}
    \\end{center}'''
    % (latex(y2 + 0.6), latex(a_val), latex(b_val), latex(d_val), latex(y2), latex(y2), latex(y2), latex(y1), latex(y1), latex(y1), latex(y2))
    )

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Công thức xác định tốc độ tăng trưởng doanh thu của công ty là $f(t) = %s$' % (latex(f_expr))
    nb_da_1_s = 'Công thức xác định tốc độ tăng trưởng doanh thu của công ty là $f(t) = %s$' % (latex(wrong_f_expr))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Dựa vào đồ thị hàm số $y = f(t) = a t^3 + b t^2 + c t + d$ ($a \\neq 0$), ta có: \\\\
    1) Đồ thị đi qua điểm $(0; %s)$ và đạt cực tiểu tại điểm đó nên $d = %s$ và $f'(0) = c = 0$. \\\\
    2) Đồ thị đạt cực đại tại điểm $(1; %s)$ nên $f'(1) = 0$ và $f(1) = %s$. \\\\
    Ta có $f'(t) = 3a t^2 + 2b t$. \\\\
    Do $f'(1) = 0 \\Leftrightarrow 3a + 2b = 0 \\Leftrightarrow b = -\\frac{3}{2}a$. \\\\
    Mặt khác $f(1) = %s \\Leftrightarrow a + b + %s = %s \\Leftrightarrow a - \\frac{3}{2}a = %s \\Leftrightarrow a = %s$. \\\\
    Suy ra $b = %s$. \\\\
    Vậy công thức xác định tốc độ tăng trưởng doanh thu của công ty là $f(t) = %s$.'''
    % (latex(y1), latex(y1), latex(y2), latex(y2), latex(y2), latex(y1), latex(y2), latex(y2 - y1), latex(a_val), latex(b_val), latex(f_expr))
    )

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Doanh thu của công ty đạt tốc độ tăng trưởng cực đại tại thời điểm $t = 1$ năm'
    th_da_1_s = 'Doanh thu của công ty đạt tốc độ tăng trưởng cực đại tại thời điểm $t = 2$ năm'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có $f'(t) = %s$. \\\\
    $f'(t) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow t = 0$ hoặc $t = 1$. \\\\
    Bảng biến thiên của hàm số $f(t)$ trên $[0; +\\infty)$: \\\\
    \\begin{center}
    \\begin{tikzpicture}
    \\tkzTabInit[espcl=2.5,lgt=1.5]{$t$/1,$f'(t)$/0.7,$f(t)$/2.1}{$0$,$1$,$+\\infty$}
    \\tkzTabLine{0,+,0,-}
    \\tkzTabVar{-/$%s$,+/$%s$,-/$-\\infty$}
    \\end{tikzpicture}
    \\end{center}
    Dựa vào bảng biến thiên, hàm số $f(t)$ đạt cực đại tại $t = 1$. Vậy doanh thu của công ty đạt tốc độ tăng trưởng cực đại tại thời điểm $t = 1$ năm.'''
    % (latex(f_prime), latex(f_prime), latex(y1), latex(y2))
    )

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Trong năm đầu tiên ($0 \\le t \\le 1$), tốc độ tăng trưởng doanh thu của công ty luôn có xu hướng tăng'
    vd_da_1_s = 'Trong năm đầu tiên ($0 \\le t \\le 1$), tốc độ tăng trưởng doanh thu của công ty luôn có xu hướng giảm'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Trong khoảng $0 < t < 1$, ta có $f'(t) = %s > 0$ nên hàm số $y = f(t)$ đồng biến trên $[0; 1]$. \\\\
    Do đó, trong năm đầu tiên ($0 \\le t \\le 1$), tốc độ tăng trưởng doanh thu của công ty luôn có xu hướng tăng.'''
    % (latex(f_prime))
    )

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Tại thời điểm $t = 1,5$ năm, tốc độ tăng trưởng doanh thu của công ty đạt giá trị bằng $%s$ tỷ đồng/năm' % (val_1_5_str)
    vdc_da_1_s = 'Tại thời điểm $t = 1,5$ năm, tốc độ tăng trưởng doanh thu của công ty đạt giá trị bằng $%s$ tỷ đồng/năm' % (wrong_val_1_5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Thay $t = 1,5$ vào công thức $f(t) = %s$, ta được: \\\\
    $f(1,5) = %s$. \\\\
    Vậy tại thời điểm $t = 1,5$ năm, tốc độ tăng trưởng doanh thu của công ty đạt giá trị bằng $%s$ tỷ đồng/năm.'''
    % (latex(f_expr), latex(f_expr.subs(t, Rational(3, 2))), val_1_5_str)
    )

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
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n' +
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

