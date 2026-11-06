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


def bt_dang16_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số để tạo bài toán mới nhưng luôn giữ cấu trúc bài mẫu
            # Chọn a là số lẻ để khi chia 2 tạo ra phân số đẹp (giống bài gốc a = 3 -> 3/2)
            a_val = random.choice([3, 5, 7, 9])

            # Random hệ số cho câu d (c1*m - c2*n)
            c1 = random.randint(2, 4)
            c2 = random.randint(1, 3)
            giatri_d = c1 * (-1) - c2 * a_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x) = \\sqrt{%sx - x^2}$.''' % (a_val))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $y = f(x)$ đồng biến trên khoảng $\\left(0; %s\\right)$' % latex(Rational(a_val, 2))
            nb_da_1_s = 'Hàm số $y = f(x)$ đồng biến trên khoảng $\\left(%s; %s\\right)$' % (latex(Rational(a_val, 2)), a_val)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hàm số $y = f(x)$ đạt cực đại tại $x = %s$' % latex(Rational(a_val, 2))
            th_da_1_s = 'Hàm số $y = f(x)$ đạt cực tiểu tại $x = %s$' % latex(Rational(a_val, 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Giá trị lớn nhất của hàm số trên $[0; %s]$ bằng $%s$' % (a_val, latex(Rational(a_val, 2)))
            vd_da_1_s = 'Giá trị lớn nhất của hàm số trên $[0; %s]$ bằng $%s$' % (a_val, a_val)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Gọi $d$ là đường thẳng đi qua điểm cực trị của đồ thị hàm số và cắt hai tia $Ox, Oy$ lần lượt tại hai điểm $A, B$. Khi diện tích tam giác $OAB$ nhỏ nhất, phương trình đường thẳng $d$ có dạng $y = mx + n$ thì $%sm - %sn$ là một số âm' % (c1, c2)
            vdc_da_1_s = 'Gọi $d$ là đường thẳng đi qua điểm cực trị của đồ thị hàm số và cắt hai tia $Ox, Oy$ lần lượt tại hai điểm $A, B$. Khi diện tích tam giác $OAB$ nhỏ nhất, phương trình đường thẳng $d$ có dạng $y = mx + n$ thì $%sm - %sn$ là một số dương' % (c1, c2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

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

            # Sinh lời giải động dựa trên đáp án được chọn ngẫu nhiên
            if '\\True' in nb_da_1:
                loigiai_nb_1 = 'Dựa vào bảng biến thiên, ta thấy hàm số đồng biến trên khoảng $\\left(0; %s\\right)$. Do đó mệnh đề đúng.' % latex(Rational(a_val, 2))
            else:
                loigiai_nb_1 = 'Dựa vào bảng biến thiên, ta thấy hàm số đồng biến trên khoảng $\\left(0; %s\\right)$ và nghịch biến trên khoảng $\\left(%s; %s\\right)$. Do đó mệnh đề sai.' % (latex(Rational(a_val, 2)), latex(Rational(a_val, 2)), a_val)

            if '\\True' in th_da_1:
                loigiai_th_1 = 'Dựa vào bảng biến thiên ta suy ra hàm số đạt cực đại tại $x = %s$. Do đó mệnh đề đúng.' % latex(Rational(a_val, 2))
            else:
                loigiai_th_1 = 'Dựa vào bảng biến thiên ta suy ra hàm số đạt cực đại tại $x = %s$ (không có cực tiểu). Do đó mệnh đề sai.' % latex(Rational(a_val, 2))

            if '\\True' in vd_da_1:
                loigiai_vd_1 = 'Ta có $f(x) = \\sqrt{%sx - x^2} \\le \\sqrt{\\frac{%s}{4}} = %s, \\forall x \\in [0; %s]$. Dấu "=" xảy ra khi $x = %s$. Do đó mệnh đề đúng.' % (a_val, a_val**2, latex(Rational(a_val, 2)), a_val, latex(Rational(a_val, 2)))
            else:
                loigiai_vd_1 = 'Ta có $f(x) = \\sqrt{%sx - x^2} \\le \\sqrt{\\frac{%s}{4}} = %s, \\forall x \\in [0; %s]$. Dấu "=" xảy ra khi $x = %s$. Do đó mệnh đề sai.' % (a_val, a_val**2, latex(Rational(a_val, 2)), a_val, latex(Rational(a_val, 2)))

            loigiai_vdc_base = ('''Đồ thị hàm số có một điểm cực trị là $I\\left(%s; %s\\right)$. \\\\
            Gọi $A(a; 0); B(0; b)$ trong đó $a > 0, b > 0$. Khi đó đường thẳng $d$ có phương trình là: $\\frac{x}{a} + \\frac{y}{b} = 1$. \\\\
            Do $I \\in d \\Rightarrow \\frac{%s}{a} + \\frac{%s}{b} = 1 \\Rightarrow \\frac{1}{a} + \\frac{1}{b} = \\frac{2}{%s}$ (1). \\\\
            Tam giác $OAB$ vuông tại $O$ nên diện tích $S_{\\triangle OAB} = \\frac{1}{2} OA \\cdot OB = \\frac{1}{2} ab$. \\\\
            Do $a, b$ là các số dương nên $\\frac{1}{a} + \\frac{1}{b} \\ge 2\\sqrt{\\frac{1}{a} \\cdot \\frac{1}{b}} \\Leftrightarrow \\frac{2}{%s} \\ge 2\\sqrt{\\frac{1}{ab}} \\Leftrightarrow \\frac{1}{%s} \\ge \\frac{1}{\\sqrt{ab}} \\Leftrightarrow ab \\ge %s$. \\\\
            Xét $ab = %s \\Leftrightarrow a = b = %s$. Suy ra $S_{\\triangle OAB} \\ge \\frac{%s}{2}$. \\\\
            $S_{\\triangle OAB} = \\frac{%s}{2} \\Leftrightarrow a = b = %s$ hay diện tích tam giác $OAB$ nhỏ nhất bằng $\\frac{%s}{2}$ khi $a = b = %s \\Rightarrow (d)$ có phương trình $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow y = -x + %s \\Rightarrow \\left\\{\\begin{array}{l} m = -1 \\\\ n = %s \\end{array}\\right. \\Rightarrow %sm - %sn = %s$. ''' % (
                latex(Rational(a_val, 2)), latex(Rational(a_val, 2)), 
                latex(Rational(a_val, 2)), latex(Rational(a_val, 2)), a_val,
                a_val, a_val, a_val**2,
                a_val**2, a_val, a_val**2,
                a_val**2, a_val, a_val**2, a_val,
                a_val, a_val, a_val, a_val,
                c1, c2, giatri_d
            ))

            if '\\True' in vdc_da_1:
                loigiai_vdc_1 = loigiai_vdc_base + 'Vì $%s < 0$ nên mệnh đề đúng.' % giatri_d
            else:
                loigiai_vdc_1 = loigiai_vdc_base + 'Vì $%s < 0$ nên mệnh đề sai.' % giatri_d

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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

            # Khối Lời giải chung (Tập xác định, Đạo hàm và Bảng biến thiên - VẼ TIKZ THỦ CÔNG ĐÃ FIX)
            loigiai_chung = ('''Tập xác định của hàm số là $D = [0; %s]$. \\\\
            Ta có $f'(x) = \\frac{%s - 2x}{2\\sqrt{%sx - x^2}}$. \\\\
            $f'(x) = 0 \\Leftrightarrow \\frac{%s - 2x}{2\\sqrt{%sx - x^2}} = 0 \\Leftrightarrow %s - 2x = 0 \\Leftrightarrow x = %s$. \\\\
            Hàm số không tồn tại đạo hàm tại $x = 0; x = %s$. \\\\
            Bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\def\\w{1.5}
            \\def\\c{2.2}
            \\draw (0,0) rectangle (\\w+4*\\c, -4.5);
            \\draw (0,-1) -- (\\w+4*\\c, -1);
            \\draw (0,-2) -- (\\w+4*\\c, -2);
            \\draw (\\w,0) -- (\\w,-4.5);
            \\node at (\\w/2, -0.5) {$x$};
            \\node at (\\w/2, -1.5) {$f'(x)$};
            \\node at (\\w/2, -3.25) {$f(x)$};
            \\node at (\\w+0.5*\\c, -0.5) {$-\\infty$};
            \\node at (\\w+1*\\c, -0.5) {$0$};
            \\node at (\\w+2*\\c, -0.5) {$%s$};
            \\node at (\\w+3*\\c, -0.5) {$%s$};
            \\node at (\\w+3.5*\\c, -0.5) {$+\\infty$};
            \\begin{scope}
                \\clip (\\w, -1) rectangle (\\w+1*\\c-0.06, -4.5);
                \\foreach \\i in {0, 2, ..., 150}
                    \\draw[thin, gray] (\\i/10, -1) -- (\\i/10 - 3.5, -4.5);
            \\end{scope}
            \\begin{scope}
                \\clip (\\w+3*\\c+0.06, -1) rectangle (\\w+4*\\c, -4.5);
                \\foreach \\i in {0, 2, ..., 150}
                    \\draw[thin, gray] (\\i/10, -1) -- (\\i/10 - 3.5, -4.5);
            \\end{scope}
            \\draw (\\w+1*\\c-0.04, -1) -- (\\w+1*\\c-0.04, -4.5);
            \\draw (\\w+1*\\c+0.04, -1) -- (\\w+1*\\c+0.04, -4.5);
            \\draw (\\w+3*\\c-0.04, -1) -- (\\w+3*\\c-0.04, -4.5);
            \\draw (\\w+3*\\c+0.04, -1) -- (\\w+3*\\c+0.04, -4.5);
            \\node at (\\w+2*\\c, -1.5) {$0$};
            \\node at (\\w+1.5*\\c, -1.5) {$+$};
            \\node at (\\w+2.5*\\c, -1.5) {$-$};
            \\node (A) at (\\w+1*\\c+0.3, -4) {$0$};
            \\node (B) at (\\w+2*\\c, -2.5) {$%s$};
            \\node (C) at (\\w+3*\\c-0.3, -4) {$0$};
            \\draw[->] (A) -- (B);
            \\draw[->] (B) -- (C);
            \\end{tikzpicture}
            \\end{center}''' % (a_val, a_val, a_val, a_val, a_val, a_val, latex(Rational(a_val, 2)), a_val, latex(Rational(a_val, 2)), a_val, latex(Rational(a_val, 2))))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n' +
                str(loigiai_chung) + '\n' +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

