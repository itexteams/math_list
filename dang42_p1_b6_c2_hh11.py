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


def bt_dang42_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B3: Suy nghĩ tìm cách random bài toán
            # Ta sẽ random hệ số k của cạnh a (ví dụ k thuộc {1, 2, 3})
            k = random.randint(1, 4)
            side = k * a

            # Tính toán các thành phần của bài toán
            # Diện tích đáy ABC (tam giác đều): S = (side^2 * sqrt(3)) / 4
            s_abc = Rational(k**2, 4) * sqrt(3) * a**2

            # AM là đường cao tam giác đều: AM = (side * sqrt(3)) / 2
            am = Rational(k, 2) * sqrt(3) * a

            # Vì góc giữa SA và (SBC) bằng 45 độ, tam giác SAM vuông cân tại A
            # => SA = AM
            sa = am

            # Thể tích V = 1/3 * SA * S_ABC
            # V = 1/3 * (k*a*sqrt(3)/2) * (k^2*a^2*sqrt(3)/4)
            # V = (k^3 * a^3 * 3) / 24 = (k^3 * a^3) / 8
            v_num = k**3
            v_den = 8
            v_final = Rational(v_num, v_den) * a**3

            # B4: Điều chỉnh các phương án sai
            def get_distractors(k, v_final):
                ans_list = []
                # Phương án đúng
                correct = '$%s$' % (latex(v_final))

                # Các phương án sai dựa theo mẫu trong ảnh: 3a^3/8, sqrt(3)a^3/12, a^3/4
                d1 = '$%s$' % (latex(Rational(3 * k**3, 8) * a**3))
                d2 = '$%s$' % (latex(Rational(k**3, 12) * sqrt(3) * a**3))
                d3 = '$%s$' % (latex(Rational(k**3, 4) * a**3))

                distractors = [d1, d2, d3]
                # Đảm bảo không trùng lặp (dù với k khác nhau các giá trị này thường khác nhau)
                final_s = list(set(distractors))
                while len(final_s) < 3:
                    random_val = Rational(random.randint(1, 10), random.randint(2, 10)) * a**3
                    if '$%s$' % latex(random_val) != correct:
                        final_s.append('$%s$' % latex(random_val))

                return correct, final_s

            da_dung, list_sai = get_distractors(k, v_final)

            # Nội dung hình vẽ TikZ (Độ dày nét 1pt)
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[line cap=round,line join=round, line width=1pt, scale=1]
                % Định nghĩa các điểm
                \coordinate (A) at (0,0);
                \coordinate (B) at (-1.5,-1.5);
                \coordinate (C) at (3,-1);
                \coordinate (S) at (0,3.5);
                \coordinate (M) at ($(B)!0.5!(C)$);
                \coordinate (H) at ($(S)!0.6!(M)$);
                \draw [dash pattern=on 3pt off 3pt] (S)--(A) (A)--(B) (A)--(C) (A)--(M) (A)--(H);
                \draw (S)--(B)--(C)--(S) (S)--(M);
                \draw (0,0.3)--(-0.3,0.3)--(-0.3,0); % Góc tại A (SA vuông đáy)
                \draw (S) node[above] {$S$};
                \draw (A) node[left] {$A$};
                \draw (B) node[below left] {$B$};
                \draw (C) node[right] {$C$};
                \draw (M) node[below right] {$M$};
                \draw (H) node[above right] {$H$};
                \fill (S) circle (1.2pt) (A) circle (1.2pt) (B) circle (0pt) (C) circle (0pt) (M) circle (0pt) (H) circle (0pt);
            \end{tikzpicture}
            \end{center}"""

            # B2: Viết lại nội dung câu hỏi
            side_text = latex(side)
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $%s$, cạnh bên $SA$ vuông góc với mặt phẳng đáy, góc giữa $SA$ và mặt phẳng $\\left(SBC\\right)$ bằng $45^\\circ$. Thể tích khối chóp $S.ABC$ bằng'''
                            % (side_text))

            # Nội dung lời giải chi tiết
            loigiai = ('''%s
            Gọi $M$ là trung điểm $BC$ thì $AM \\perp BC$ và $SA \\perp BC$ nên $BC \\perp \\left(SAM\\right)$. \\\\
            Kẻ $AH \\perp SM$ tại $H$ thì $AH \\perp \\left(SBC\\right)$. Suy ra góc giữa $SA$ và mặt phẳng $\\left(SBC\\right)$ bằng \\\\
            $\\widehat{ASH} = \\widehat{ASM} = 45^\\circ$. Do đó, $\\Delta SAM$ vuông cân ở $A$ và $SA = AM = \\frac{%s \\cdot \\sqrt{3}}{2} = %s$. \\\\
            Diện tích tam giác đều $ABC$ là $S_{ABC} = \\frac{\\left(%s\\right)^2 \\sqrt{3}}{4} = %s$. \\\\
            Suy ra $V_{S.ABC} = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.''' 
                        % (tikz_code, side_text, latex(am), side_text, latex(s_abc), latex(sa), latex(s_abc), latex(v_final)))

            # Đưa các đáp án vào danh sách
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + list_sai
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

