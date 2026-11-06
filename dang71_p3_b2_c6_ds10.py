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


def bt_dang71_p3_b2_c6_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Mỗi màu gồm k bóng được đánh số từ 1 đến k (đề bài gốc k = 7, tổng 3*k = 21 bóng)
        k = choice([6, 7])
        total_balls = 3 * k


        omega = 1
        for i in range(7):
            omega *= (total_balls - i)



        T_val = (k - 1) * (k - 2) * (k - 3)
        nV_val = T_val - 3 * (k - 2) * (k - 3) + 3 * (k - 3) - 1

        # Số phần tử của biến cố:
        n_A = 6 * k * T_val * nV_val

        # Xác suất P = m / n dưới dạng phân số tối giản
        p_frac = frac(n_A, omega)
        m_val = p_frac.numerator
        n_val = p_frac.denominator

        # Đặt biểu thức câu hỏi n - C * m^2 sao cho ra số nguyên
        # Với k = 7: P = 71 / 116280, n - 22*m^2 = 5378
        # Với k = 6: P = 2 / 4641, n - 22*m^2 = 4553
        coeff = 22
        ans_val = n_val - coeff * (m_val ** 2)
        kq_str = str(ans_val)

        # Hình vẽ TikZ
        hinhve = '''\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (-2,0);
    \\coordinate (B) at (-1,-1.732);
    \\coordinate (C) at (1,-1.732);
    \\coordinate (D) at (2,0);
    \\coordinate (E) at (1,1.732);
    \\coordinate (F) at (-1,1.732);
    \\fill[green!10] (A)--(B)--(C)--(D)--(E)--(F)--cycle;
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--(F)--cycle;
    \\draw[line width=1pt] (A)--(D) (B)--(E) (C)--(F);
    \\filldraw[fill=white, line width=1pt] (O) circle (2pt) node[below=2pt] {$O$};
    \\filldraw[fill=white, line width=1pt] (A) circle (2pt) node[left] {$A$};
    \\filldraw[fill=white, line width=1pt] (B) circle (2pt) node[below left] {$B$};
    \\filldraw[fill=white, line width=1pt] (C) circle (2pt) node[below right] {$C$};
    \\filldraw[fill=white, line width=1pt] (D) circle (2pt) node[right] {$D$};
    \\filldraw[fill=white, line width=1pt] (E) circle (2pt) node[above right] {$E$};
    \\filldraw[fill=white, line width=1pt] (F) circle (2pt) node[above left] {$F$};
    \\end{tikzpicture}'''

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Có $%s$ bóng đèn gồm $3$ màu đỏ, xanh, vàng, mỗi màu gồm $%s$ bóng được đánh số từ $1$ đến $%s$. Chọn ngẫu nhiên $7$ bóng và gắn vào các vị trí $O, A, B, C, D, E, F$ như hình vẽ, $ABCDEF$ là lục giác đều tâm $O$. Gọi $P$ là xác suất để hai bóng đèn ở hai vị trí kề nhau luôn khác màu, đồng thời ba bóng đèn trên mỗi đường chéo qua tâm $AD, BE, CF$ có số đôi một khác nhau. Biết $P = \\dfrac{m}{n}$ ($m, n$ nguyên dương và phân số $\\dfrac{m}{n}$ tối giản). Giá trị $n - %sm^2$ bằng bao nhiêu?}{%s}'''
                         % (str(total_balls), str(k), str(k), str(coeff), hinhve))



        # Nội dung lời giải
        loigiai = ('''Số phần tử của không gian mẫu là số cách chọn $7$ bóng đèn từ $%s$ bóng đèn rồi xếp vào $7$ vị trí phân biệt $O, A, B, C, D, E, F$: \\\\
                   $n(\\Omega) = A_{%s}^7 = %s$. \\\\
                   Xét biến cố thỏa mãn yêu cầu bài toán: \\\\
                   \\textbf{Bước 1: Phân phối màu cho các vị trí} \\\\
                   + Vị trí tâm $O$ kề với cả $6$ đỉnh $A, B, C, D, E, F$ nên $O$ có thể nhận một trong $3$ màu (có $3$ cách chọn màu cho $O$). \\\\
                   + Giả sử $O$ nhận màu đỏ, khi đó $6$ đỉnh ở chu vi lục giác đều chỉ được mang hai màu còn lại là xanh và vàng. Để hai đỉnh kề nhau luôn khác màu, các đỉnh phải mang màu xen kẽ nhau: \\\\
                   Trường hợp 1: $A, C, E$ mang màu xanh và $B, D, F$ mang màu vàng. \\\\
                   Trường hợp 2: $A, C, E$ mang màu vàng và $B, D, F$ mang màu xanh. \\\\
                   Như vậy có $3 \\times 2 = 6$ cách tô màu hợp lệ cho $7$ vị trí. Khi đó, trên mỗi đường chéo qua tâm ($AD, BE, CF$), ba vị trí luôn nhận đủ $3$ màu phân biệt (đỏ, xanh, vàng). \\\\
                   \\textbf{Bước 2: Gán số cho các bóng đèn} \\\\
                   Xét trường hợp $O$ mang màu đỏ, $A, C, E$ mang màu xanh và $D, F, B$ mang màu vàng: \\\\
                   + Có $%s$ cách chọn một bóng đèn màu đỏ gắn vào vị trí $O$. Giả sử bóng này mang số $s_0$. \\\\
                   + Vì ba bóng trên mỗi đường chéo $AD, BE, CF$ có số đôi một khác nhau nên không có bóng nào tại các đỉnh $A, B, C, D, E, F$ được mang số $s_0$. Do đó, các bóng đèn ở $6$ đỉnh này phải lấy từ tập $%s$ số khác $s_0$. \\\\
                   + Chọn $3$ bóng màu xanh gắn vào $3$ vị trí $A, C, E$: Số cách chọn và sắp xếp $3$ số phân biệt là $A_{%s}^3 = %s$ cách. \\\\
                   + Chọn $3$ bóng màu vàng gắn vào $3$ vị trí $D, F, B$: Giả sử số tại $A, C, E$ lần lượt là $x_A, x_C, x_E$. Ta cần chọn $3$ số phân biệt $x_D, x_F, x_B$ từ tập $%s$ số nói trên sao cho $x_D \\neq x_A, x_F \\neq x_C, x_B \\neq x_E$. \\\\
                   Áp dụng nguyên lí bao hàm - loại trừ: \\\\
                   - Tổng số bộ $3$ số phân biệt bất kì là: $A_{%s}^3 = %s$. \\\\
                   - Số bộ có ít nhất $1$ vị trí trùng số với đỉnh đối diện: $3 \\times A_{%s}^2 = 3 \\times %s = %s$. \\\\
                   - Số bộ có ít nhất $2$ vị trí trùng số với đỉnh đối diện: $3 \\times A_{%s}^1 = 3 \\times %s = %s$. \\\\
                   - Số bộ có cả $3$ vị trí đều trùng số với đỉnh đối diện: $1$. \\\\
                   Suy ra số cách xếp số cho các bóng tại $D, F, B$ là: \\\\
                   $%s - %s + %s - 1 = %s$ cách. \\\\
                   Do đó, số cách chọn và gắn bóng đèn thỏa mãn là: \\\\
                   $n(A) = 6 \\times %s \\times %s \\times %s = %s$. \\\\
                   Xác suất cần tìm là: \\\\
                   $P = \\dfrac{n(A)}{n(\\Omega)} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$. \\\\
                   Suy ra $m = %s$, $n = %s$. \\\\
                   Vậy giá trị của biểu thức là: $n - %sm^2 = %s - %s \\times %s^2 = %s$.'''
                   % (str(total_balls),
                      str(total_balls), str(omega),
                      str(k),
                      str(k - 1),
                      str(k - 1), str(T_val),
                      str(k - 1),
                      str(k - 1), str(T_val),
                      str(k - 2), str((k - 2) * (k - 3)), str(3 * (k - 2) * (k - 3)),
                      str(k - 3), str(k - 3), str(3 * (k - 3)),
                      str(T_val), str(3 * (k - 2) * (k - 3)), str(3 * (k - 3)), str(nV_val),
                      str(k), str(T_val), str(nV_val), str(n_A),
                      str(n_A), str(omega), str(m_val), str(n_val),
                      str(m_val), str(n_val),
                      str(coeff), str(n_val), str(coeff), str(m_val), str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')
    return content

