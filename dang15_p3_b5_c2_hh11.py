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


def bt_dang15_p3_b5_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số k cho tỉ lệ vectơ
                k = random.choice([2, 3, 4, 5])

                # Tính tỉ số MS/AS = k / (k+2)
                # Khoảng cách = 2 * (MS/AS) * d(H,(SCD)) = (2k / (k+2)) * (a*sqrt(15) / 5)
                # Phân số phần hệ số: (2k) / (5(k+2))
                num = 2 * k
                den = 5 * (k + 2)

                # Rút gọn phân số để tìm m, p
                fraction = frac(num, den)
                m = fraction.numerator
                p = fraction.denominator
                n = 15

                T = m + n + p

                # Đoạn code TikZ vẽ hình chóp (đã xóa các ký tự % gây lỗi)
                tikz_img = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=1.2]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (1.5,-1.5);
            \\coordinate (C) at (4.5,-1.5);
            \\coordinate (D) at (6,0);
            \\coordinate (H) at (3,0);
            \\coordinate (S) at (3,4);
            \\coordinate (K) at (5.2, -0.75);
            \\draw [dashed] (A) -- (D) (S) -- (H) (B) -- (H) -- (C) (H) -- (K);
            \\draw (A) -- (B) -- (C) -- (D) (S) -- (A) (S) -- (B) (S) -- (C) (S) -- (D) (S) -- (K);
            \\coordinate (I) at ($(H)!1/(1+%s)!(S)$);
            \\coordinate (M) at ($(A)!2/(2+%s)!(S)$);
            \\draw [dashed] (D) -- (M);
            \\draw [dashed] (S) -- (H);
            \\coordinate (O) at ($(S)!0.6!(K)$);
            \\draw [dashed] (H) -- (O);
            \\fill (A) circle (1pt) node[left] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
            \\fill (C) circle (1pt) node[below] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (H) circle (1pt) node[above left] {$H$};
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (K) circle (1pt) node[right] {$K$};
            \\fill (I) circle (1pt) node[above left] {$I$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (O) circle (1pt) node[right] {$O$};
            \\end{tikzpicture}
            \\end{center}''' % (k, k))

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là nửa lục giác đều tâm $H$, cạnh bằng $a$, $AD = 2a$. $\\Delta SAD$ là tam giác đều và nằm trong mặt phẳng vuông góc với đáy. Điểm $I$ thuộc $SH$ sao cho $\\overrightarrow{IS} = -%s\\overrightarrow{IH}$. Gọi $M$ là giao điểm của $DI$ và $SA$. Biết $d(M, (SCD)) = \\frac{ma\\sqrt{n}}{p}$ với $m, n, p$ là các số nguyên dương và $m < n < p < 30$. Giá trị biểu thức $T = m+n+p$ bằng bao nhiêu?''' % (k))

                # Đáp án đúng
                da = '$T = %s$' % T

                # Các đáp án nhiễu
                distractors = set()
                distractors.add('$T = %s$' % (T + 2))
                distractors.add('$T = %s$' % (T - 2))
                distractors.add('$T = %s$' % (T + 5))
                distractors.add('$T = %s$' % (T - 5))

                # Mô phỏng sai lầm khi không rút gọn phân số (nếu có thể)
                if num != m:
                    fake_T = num + n + den
                    distractors.add('$T = %s$' % fake_T)

                wrong_choices = random.sample(list(distractors), 3)

                das1 = str(wrong_choices[0])
                das2 = str(wrong_choices[1])
                das3 = str(wrong_choices[2])

                da_d = ('\\True ' + str(da))

                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Lời giải
                if k % 2 == 0:
                    sm_ma_frac = "%s" % (k // 2)
                else:
                    sm_ma_frac = "\\frac{%s}{2}" % k

                loigiai = ('''%s Vì 3 điểm $M, I, D$ thẳng hàng nên áp dụng định lý Menelaus trong $\\Delta SAH$ ta có:\\\\
            $\\frac{SM}{MA} \\cdot \\frac{AD}{DH} \\cdot \\frac{HI}{IS} = 1 \\Leftrightarrow \\frac{SM}{MA} \\cdot \\frac{2}{1} \\cdot \\frac{1}{%s} = 1 \\Leftrightarrow \\frac{SM}{MA} = %s \\Rightarrow \\frac{MS}{AS} = \\frac{%s}{%s}$.\\\\
            Suy ra $d(M, (SCD)) = \\frac{%s}{%s}d(A, (SCD)) = \\frac{%s}{%s} \\cdot 2d(H, (SCD)) = \\frac{%s}{%s}d(H, (SCD))$.\\\\
            Kẻ $HK \\perp CD$ tại $K$. Vì $ABCD$ là nửa lục giác đều tâm $H$ nên $\\Delta HCD$ đều cạnh bằng $a$.\\\\
            Khi đó, $HK = \\frac{a\\sqrt{3}}{2}$.\\\\
            Kẻ $HO \\perp SK$ tại $O$. Khi đó, vì $\\begin{cases} HO \\perp SK \\\\ HO \\perp CD \\end{cases} \\Rightarrow HO \\perp (SCD) \\Rightarrow d(H, (SCD)) = HO$.\\\\
            Xét $\\Delta SHK$ có $HK = \\frac{a\\sqrt{3}}{2}, SH = \\frac{2a\\sqrt{3}}{2} = a\\sqrt{3} \\\\ \\Rightarrow HO = \\frac{SH \\cdot HK}{\\sqrt{SH^2 + HK^2}} = \\frac{a\\sqrt{3} \\cdot \\frac{a\\sqrt{3}}{2}}{\\sqrt{3a^2 + \\frac{3a^2}{4}}} = \\frac{a\\sqrt{15}}{5}$.\\\\
            Do đó: $d(M, (SCD)) = \\frac{%s}{%s} \\cdot \\frac{a\\sqrt{15}}{5} = \\frac{%s a\\sqrt{15}}{%s}$ nên $T = m + n + p = %s + %s + %s = %s$.'''
                % (tikz_img,k, sm_ma_frac, k, k+2, k, k+2, k, k+2, 2*k, k+2, 2*k, k+2, m, p, m, n, p, T))
                dapan='\\shortans[0]{$%s$}\n'%(T)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

