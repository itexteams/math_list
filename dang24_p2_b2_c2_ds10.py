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


def bt_dang24_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên
            Px = random.choice([20, 30, 40, 50])
            Py = random.choice([30, 40, 50, 60])
            xt = random.choice([2, 3])
            yt = random.choice([3, 4])
            xf = random.choice([5, 6])
            yf = random.choice([6, 7])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong một cuộc thi pha chế, mỗi đội chơi được sử dụng tối đa $24$g hương liệu, $9$ lít nước và $210$g đường để pha chế nước cam và nước táo. Để pha chế $1$ lít nước cam cần $30$g đường, $1$ lít nước và $1$g hương liệu; để pha chế $1$ lít nước táo cần $10$g đường, $1$ lít nước và $4$g hương liệu. Mỗi lít nước cam nhận được $%s$ điểm thưởng, mỗi lít nước táo nhận được $%s$ điểm thưởng. Giả sử $x,y$ lần lượt là số lít nước cam và số lít nước táo mà mỗi đội cần pha chế.'''
                             % (Px, Py))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Nguyên liệu mà mỗi đội được sử dụng có thể pha được $%s$ lít nước cam và $%s$ lít nước táo' % (xt, yt)
            nb_da_1_s = 'Nguyên liệu mà mỗi đội được sử dụng có thể pha được $%s$ lít nước cam và $%s$ lít nước táo' % (xf, yf)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1_d = ('''Thử với $x=%s, y=%s$, ta có: \\\\
            Lượng đường cần dùng là $30 \\cdot %s + 10 \\cdot %s = %s \\le 210$. \\\\
            Lượng nước cần dùng là $1 \\cdot %s + 1 \\cdot %s = %s \\le 9$. \\\\
            Lượng hương liệu cần dùng là $1 \\cdot %s + 4 \\cdot %s = %s \\le 24$. \\\\
            Vậy có thể pha được $%s$ lít nước cam và $%s$ lít nước táo.'''
                            % (xt, yt, xt, yt, 30*xt+10*yt, xt, yt, xt+yt, xt, yt, xt+4*yt, xt, yt))

            loigiai_nb_1_s = ('''Thử với $x=%s, y=%s$, ta có: \\\\
            Lượng đường cần dùng là $30 \\cdot %s + 10 \\cdot %s = %s > 210$ (không thỏa mãn). \\\\
            Lượng nước cần dùng là $1 \\cdot %s + 1 \\cdot %s = %s \\le 9$. \\\\
            Lượng hương liệu cần dùng là $1 \\cdot %s + 4 \\cdot %s = %s > 24$ (không thỏa mãn). \\\\
            Vậy không thể pha được $%s$ lít nước cam và $%s$ lít nước táo.'''
                            % (xf, yf, xf, yf, 30*xf+10*yf, xf, yf, xf+yf, xf, yf, xf+4*yf, xf, yf))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Điều kiện về lượng đường mà đội cần sử dụng là $30x + 10y \\le 210$'
            th_da_1_s = 'Điều kiện về lượng đường mà đội cần sử dụng là $30x + 10y \\ge 210$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Đội sử dụng $x$ lít nước cam và $y$ lít nước táo. Mỗi lít nước cam cần $30$g đường, mỗi lít nước táo cần $10$g đường. Do đó lượng đường cần sử dụng là $30x + 10y$. Vì tối đa có $210$g đường nên ta có điều kiện $30x + 10y \\le 210$.''')

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hệ điều kiện về nguyên liệu của đội có thể sử dụng là: $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ 3x + y \\le 21 \\\\ x + y \\le 9 \\\\ x + 4y \\le 24 \\end{cases}$'
            vd_da_1_s = 'Hệ điều kiện về nguyên liệu của đội có thể sử dụng là: $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ 3x + y \\le 21 \\\\ x + y \\ge 9 \\\\ x + 4y \\le 24 \\end{cases}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Từ các điều kiện về lượng đường, nước và hương liệu, cùng với điều kiện $x, y$ không âm, ta có hệ bất phương trình:
            \\\\ $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ 30x + 10y \\le 210 \\\\ x + y \\le 9 \\\\ x + 4y \\le 24 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ 3x + y \\le 21 \\\\ x + y \\le 9 \\\\ x + 4y \\le 24 \\end{cases}$.''')

            ########################################################################
            # Vận dụng cao ############################################
            F_0_0 = 0
            F_7_0 = Px * 7
            F_6_3 = Px * 6 + Py * 3
            F_4_5 = Px * 4 + Py * 5
            F_0_6 = Py * 6
            M = max(F_0_0, F_7_0, F_6_3, F_4_5, F_0_6)
            M_false = M + random.choice([10, 20, 30])

            vdc_da_1_d = '\\True Số điểm thưởng lớn nhất đội có thể đạt được là $%s$' % (M)
            vdc_da_1_s = 'Số điểm thưởng lớn nhất đội có thể đạt được là $%s$' % (M_false)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Số điểm thưởng đội đạt được là $F(x,y) = %sx + %sy$. \\\\
            Miền nghiệm của hệ bất phương trình là đa giác có các đỉnh $O(0;0), A(7;0), B(6;3), C(4;5), D(0;6)$.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-1,-1) rectangle (8,7);
            \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle (8,7);
            \\fill[white] (0,0) -- (7,0) -- (6,3) -- (4,5) -- (0,6) -- cycle;
            \\draw[black] (-1, 24) -- (7, 0);
            \\draw[black] (-1, 10) -- (7, 2);
            \\draw[black] (-1, 6.25) -- (7, 4.25);
            \\draw[black] (0, -1) -- (0, 7);
            \\draw[black] (-1, 0) -- (8, 0);
            \\coordinate (A) at (7,0);
            \\coordinate (B) at (6,3);
            \\coordinate (C) at (4,5);
            \\coordinate (D) at (0,6);
            \\fill (A) circle (1.5pt) node[above right] {$A$};
            \\fill (B) circle (1.5pt) node[right] {$B$};
            \\fill (C) circle (1.5pt) node[above right] {$C$};
            \\fill (D) circle (1.5pt) node[right] {$D$};
            \\draw[dashed] (6,0) node[below] {$6$} -- (6,3) -- (0,3) node[left] {$3$};
            \\draw[dashed] (4,0) node[below] {$4$} -- (4,5) -- (0,5) node[left] {$5$};
            \\node at (7,0) [below] {$7$};
            \\node at (0,6) [left] {$6$};
            \\draw[->] (-1, 0) -- (8, 0) node[below] {$x$};
            \\draw[->] (0, -1) -- (0, 7) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}
            Ta tính giá trị của $F(x,y)$ tại các đỉnh: \\\\
            $F(0;0) = 0$ \\\\
            $F(7;0) = %s$ \\\\
            $F(6;3) = %s$ \\\\
            $F(4;5) = %s$ \\\\
            $F(0;6) = %s$ \\\\
            Giá trị lớn nhất là $%s$. Vậy số điểm thưởng lớn nhất đội có thể đạt được là $%s$.'''
                             % (Px, Py, F_7_0, F_6_3, F_4_5, F_0_6, M, M))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Lựa chọn lời giải tương ứng theo phương án được chọn ở câu Nhận biết
            loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s

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

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải
            content = (
                "\\begin{minipage}{\\textwidth}\n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + "\n"
                "\\choiceTFn\n"
                "{" + str(shuffled_answers_nb[0]) + "}\n"
                "{" + str(shuffled_answers_th[0]) + "}\n"
                "{" + str(shuffled_answers_vd[0]) + "}\n"
                "{" + str(shuffled_answers_vdc[0]) + "}\n"
                "\\loigiai{\n"
                "\\begin{enumEX}[a)]{1}\n"
                "\\item " + str(shuffled_solutions_nb[0]) + "\n"
                "\\item " + str(shuffled_solutions_th[0]) + "\n"
                "\\item " + str(shuffled_solutions_vd[0]) + "\n"
                "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
                "\\end{enumEX}}\n"
                "\\end{ex}\n"
                "\\end{minipage}\n\n" )
            return content

