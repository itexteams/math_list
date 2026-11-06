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


def bt_dang25_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Chọn ngẫu nhiên bán chu vi của mỗi góc phần tư p (ở đề bài là L/4)
            # Để thuận lợi cho tính toán, chọn p trong khoảng [6, 9] tương ứng L = 4*p trong [24, 36]
            p = randint(6, 9)
            L = 4 * p

            # Giá trị x_val để tính chiều cao h ở ý b (chọn x_val sao cho (p-x)^2 - x^2/2 > 0)
            # Chọn x_val nguyên dương nhỏ hơn p
            x_val = p - 3

            # Tính chiều cao h tại x_val: h = sqrt((p - x_val)^2 - x_val^2 / 2)
            h_val_sq = (p - x_val)**2 - Rational(x_val**2, 2)
            latex_h_val = latex(sqrt(h_val_sq))

            # Tính toán các hệ số cho bài toán tìm cực trị thể tích
            # V^2 = 1/9 * x^4 * ((p-x)^2 - x^2/2) = 1/9 * x^4 * (p^2 - 2px + x^2/2) = 1/18 * (2p^2*x^4 - 4p*x^5 + x^6)
            # Đặt f(x) = 1/2 * x^6 - 2p * x^5 + p^2 * x^4 trên (0; p)
            # f'(x) = 3*x^5 - 10p*x^4 + 4p^2*x^3 = x^3 * (3*x^2 - 10p*x + 4p^2)
            # Nghiệm dương bé hơn p là x_opt = (10p - sqrt(100p^2 - 48p^2)) / 6 = (5p - p*sqrt(13)) / 3
            x_opt_val = float((5 * p - p * math.sqrt(13)) / 3)
            str_x_opt = f"{x_opt_val:.2f}".replace('.', ',')

            # Số liệu sai cho phương án a
            p_wrong_a = p * 2 - 1
            L_wrong_a = p_wrong_a * 2

            # Số liệu cho phương án c (khi các cạnh bên bằng cạnh đáy: x = p - x => x = p/2)
            x_equi = Rational(p, 2)
            latex_x_equi = latex(x_equi)
            # Diện tích giấy dán (4 mặt bên tam giác đều cạnh x_equi)
            # S = 4 * (x_equi^2 * sqrt(3) / 4) = x_equi^2 * sqrt(3)
            S_equi_val_sq = x_equi**2
            latex_S_equi = f"{latex(S_equi_val_sq)}\\sqrt{{3}}"
            latex_S_equi_wrong = f"{latex(S_equi_val_sq + randint(1, 4))}\\sqrt{{3}}"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bạn An làm đèn lồng bằng cách dùng một sợi dây đồng dài %s dm cắt thành ba đoạn để uốn làm khung đèn. Đoạn thứ nhất uốn thành hình vuông $ABCD$ có cạnh bằng $x$ (dm) để làm đáy, hai đoạn còn lại có độ dài bằng nhau uốn thành các đường gấp khúc $ASC$ và $BSD$. Khung đèn sau khi hoàn thiện có hình dạng là một hình chóp tứ giác đều $S.ABCD$ và bề mặt ngoài của đèn được dán giấy màu để trang trí, không dán mặt đáy (xem các mối nối, dán là không đáng kể). 
                             \\begin{center}
                             	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             		\\draw  [line width=1]  (117.35,115.88) -- (207.09,115.88) -- (207.09,180.49) -- (117.35,180.49) -- cycle ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (117.35,115.88) -- (207.09,180.49) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (207.09,115.88) -- (117.35,180.49) ;
                             		\\draw [line width=1]    (207.09,115.88) -- (265.55,244.59) ;
                             		\\draw [line width=1]    (117.35,180.49) -- (265.55,244.59) ;
                             		\\draw [line width=1]    (117.35,115.88) -- (56.58,243.95) ;
                             		\\draw [line width=1]    (207.09,180.49) -- (56.58,243.95) ;
                             		\\draw [line width=1]    (448.94,92.77) -- (486.25,245.21) ;
                             		\\draw [line width=1]    (448.94,92.77) -- (534.33,192.65) ;
                             		\\draw [line width=1]    (448.94,92.77) -- (366.38,244.57) ;
                             		\\draw [line width=1]    (486.25,245.21) -- (534.33,192.65) ;
                             		\\draw [line width=1]    (366.38,244.57) -- (486.25,245.21) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (448.94,92.77) -- (415.73,192.65) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (534.33,192.65) -- (415.73,192.65) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (366.38,244.57) -- (415.73,192.65) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (486.25,245.21) -- (415.73,192.65) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (534.33,192.65) -- (366.38,244.57) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (448.94,92.77) -- (450.99,218.93) ;
                             		\\draw [line width=1]    (292,170) -- (328.53,170.72) ;
                             		\\draw [shift={(332.53,170.8)}, rotate = 181.13] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                             		\\draw (99.37,92.05) node [anchor=north west][inner sep=0.75pt]    {$A$};
                             		\\draw (99.73,171.54) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             		\\draw (207.57,174.75) node [anchor=north west][inner sep=0.75pt]    {$C$};
                             		\\draw (205.93,90.39) node [anchor=north west][inner sep=0.75pt]    {$D$};
                             		\\draw (39.47,245.9) node [anchor=north west][inner sep=0.75pt]    {$S$};
                             		\\draw (267.81,247.7) node [anchor=north west][inner sep=0.75pt]    {$S$};
                             		\\draw (137.36,86.93) node [anchor=north west][inner sep=0.75pt]    {$x$ (dm)};
                             		\\draw (442.99,67.72) node [anchor=north west][inner sep=0.75pt]    {$S$};
                             		\\draw (397.73,179) node [anchor=north west][inner sep=0.75pt]    {$A$};
                             		\\draw (347.99,244.59) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             		\\draw (488.65,248.31) node [anchor=north west][inner sep=0.75pt]    {$C$};
                             		\\draw (534.31,171.77) node [anchor=north west][inner sep=0.75pt]    {$D$};
                             		\\draw (438.8,225) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             		\\draw (150.8,157) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             	\\end{tikzpicture}
                             \\end{center}'''              
                             %(L))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Độ dài cạnh bên của khung đèn bằng $(%s - x)$ dm với $0 < x < %s$' % (p, p)
            nb_da_1_s = 'Độ dài cạnh bên của khung đèn bằng $(%s - x)$ dm với $0 < x < %s$' % (p_wrong_a, L_wrong_a)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Khối chóp tứ giác đều có $4$ cạnh đáy bằng $x$ và $4$ cạnh bên bằng $l$. \\\\
            Tổng chiều dài dây: $4x + 4l = %s \\Rightarrow l = %s - x$. \\\\
            Do $l > 0 \\Rightarrow 0 < x < %s$.'''
                        % (L, p, p))

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
            th_da_1_d = '\\True Khi $x = %s$ thì độ dài đường cao của khung đèn là $%s$ dm' % (x_val, latex_h_val)  
            th_da_1_s = 'Khi $x = %s$ thì độ dài đường cao của khung đèn là $%s$ dm' % (x_val, latex(sqrt(h_val_sq + randint(1, 3))))   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Chiều cao khối chóp: $h = \\sqrt{(%s - x)^2 - \\frac{x^2}{2}}$. \\\\
            Thay $x = %s$ ta được: \\\\
            $h = \\sqrt{(%s - %s)^2 - \\frac{%s^2}{2}} = %s$ dm.'''       
                       % (p, x_val, p, x_val, x_val, latex_h_val))

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
            vd_da_1_d = '\\True Khi các cạnh bằng nhau thì diện tích giấy màu cần dùng là $%s$ dm$^2$' % (latex_S_equi)  
            vd_da_1_s = 'Khi các cạnh bằng nhau thì diện tích giấy màu cần dùng là $%s$ dm$^2$' % (latex_S_equi_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Vì các cạnh bằng nhau nên $x = %s - x \\Leftrightarrow x = %s$. \\\\
            Mỗi mặt bên là tam giác đều cạnh $%s$ dm nên diện tích giấy dán là: \\\\
            $S = 4 \\cdot \\frac{x^2\\sqrt{3}}{4} = %s \\text{ dm}^2$.'''  
                       % (p, latex_x_equi, latex_x_equi, latex_S_equi))

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
            vdc_da_1_d = '\\True Thể tích phần không gian của đèn lồng lớn nhất khi $x \\approx %s$ dm' % (str_x_opt) 
            vdc_da_1_s = 'Thể tích phần không gian của đèn lồng lớn nhất khi $x \\approx %s$ dm' % (f"{round(x_opt_val + 1.2, 2):.2f}".replace('.', ',')) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Thể tích đèn: $V = \\frac{1}{3}x^2\\sqrt{(%s - x)^2 - \\frac{x^2}{2}}$. \\\\
            Xét hàm số $f(x) = \\frac{1}{2}x^6 - %sx^5 + %sx^4$ trên $(0; %s)$. \\\\
            $f\'(x) = x^3(3x^2 - %sx + %s) = 0$ \\\\
            $\\Rightarrow x = \\frac{%s - \\sqrt{%s}}{3} \\approx %s \\in (0; %s)$. \\\\
            Lập bảng biến thiên suy ra thể tích lớn nhất khi $x \\approx %s$ dm.'''
                       % (p, 2*p, p**2, p, 10*p, 4*p**2, 5*p, 13*p**2, str_x_opt, p, str_x_opt))

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
            str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

