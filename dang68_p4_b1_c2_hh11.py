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


def bt_dang68_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hóa cạnh đáy 'a' và hệ số chiều cao 'k' (Chiều cao = k*a)
                # Trong bài gốc: k = 2
                list_k = [1, 2, 3, 4]
                k_val = random.choice(list_k)

                # Tính toán các đại lượng theo a (coi a=1 để tính toán giá trị số)
                # MN = 1/2 * BF = 1/2 * sqrt(a^2 + (ka)^2) = a*sqrt(1+k^2)/2
                # ME = 1/2 * AC = a/2
                # NE = sqrt(EC^2 + NC^2) = sqrt(3a^2/4 + (ka/2)^2) = a*sqrt(3+k^2)/2

                mn_sq = Rational(1 + k_val**2, 4)
                me_sq = Rational(1, 4)
                ne_sq = Rational(3 + k_val**2, 4)

                # Cosin góc EMN = (ME^2 + MN^2 - NE^2) / (2 * ME * MN)
                # Numerator = (1 + 1 + k^2 - 3 - k^2)/4 = -1/4
                # Denominator = 2 * (1/2) * (sqrt(1+k^2)/2) = sqrt(1+k^2)/2
                # Cos = (-1/4) / (sqrt(1+k^2)/2) = -1 / (2*sqrt(1+k^2))

                # Kết quả cos(AC, BF) là trị tuyệt đối của cos(EMN)
                mau_so = 2 * sp.sqrt(1 + k_val**2)
                kq_final = 1 / mau_so

                # Rút gọn biểu thức latex
                da_text = '$%s$' % (latex(kq_final))

                # Tạo các phương án sai bằng cách thay đổi mẫu số hoặc tử số
                s = [
                    '$%s$' % (latex(sp.sqrt(3) / (2 * sp.sqrt(1 + k_val**2)))),
                    '$%s$' % (latex(sp.sqrt(k_val + 1) / 5)),
                    '$%s$' % (latex(sp.sqrt(1 + k_val**2) / 5)),
                    '$%s$' % (latex(sp.Rational(1, 2 * k_val))),
                    '$%s$' % (latex(sp.sqrt(k_val) / 10)),
                    '$%s$' % (latex(sp.sqrt(5) / (2 * k_val + 1))),
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho lăng trụ đều $ABC.DEF$ có cạnh đáy bằng $a$, chiều cao bằng $%sa$. Tính cosin của góc tạo bởi hai đường thẳng $AC$ và $BF$.'''
                                 %(latex(k_val) if k_val != 1 else ""))

                # Hình vẽ TikZ
                tikz_code = r'''
            \begin{center}
            \begin{tikzpicture}[scale=0.8, line join=round, line cap=round, >=stealth]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.2);
                \coordinate (C) at (4,0);
                \coordinate (D) at (0,4);
                \coordinate (E) at (1.5,2.8);
                \coordinate (F) at (4,4);
                \coordinate (M) at ($(B)!0.5!(C)$);
                \coordinate (N) at ($(C)!0.5!(F)$);
                \coordinate (P) at ($(A)!0.5!(B)$);
                \draw (D)--(E)--(F)--cycle (E)--(B)--(C)--(F) (B)--(M) (A)--(B) (A)--(D) (M)--(N);
                \draw[dashed]  (A)--(C) (P)--(M) (N)--(P);
                \draw[dashed] (B)--(F);
                \fill (A)  node[left]{$A$};
                \fill (B)  node[below left]{$B$};
                \fill (C)  node[right]{$C$};
                \fill (D)  node[left]{$D$};
                \fill (E)  node[above]{$E$};
                \fill (F)  node[right]{$F$};
                \fill (M)  node[below]{$M$};
                \fill (N)  node[right]{$N$};
                \fill (P)  node[below left]{$P$};
            \end{tikzpicture}
            \end{center}'''

                # Nội dung lời giải chi tiết
                # Lưu ý: Trong code này dùng P làm trung điểm AB để tránh trùng tên với đỉnh E của lăng trụ
                loigiai = ('''Gọi $M, N, P$ lần lượt là trung điểm các đoạn thẳng $BC, CF, AB$. \\\\
                             Khi đó ta có:
                             $\\begin{cases} MN \\parallel BF \\\\ MP \\parallel AC \\end{cases} \\Rightarrow (AC; BF) = (MP; MN)$.\\\\
                             Xét tam giác $MNP$, ta tính độ dài các cạnh theo $a$: \\\\
                             $MN = \\frac{1}{2} BF = \\frac{1}{2} \\sqrt{BC^2 + CF^2} = \\frac{1}{2} \\sqrt{a^2 + (%sa)^2} = \\frac{a\\sqrt{%s}}{2}$.\\\\
                             $MP = \\frac{1}{2} AC = \\frac{a}{2}$.\\\\
                             Đoạn $CP$ là đường cao của tam giác đều đáy nên $CP = \\frac{a\\sqrt{3}}{2}$.\\\\
                             Vì $NC$ vuông góc với mặt đáy nên $NC \\perp CP$, suy ra: \\\\
                             $NP = \\sqrt{CP^2 + NC^2} = \\sqrt{\\left(\\frac{a\\sqrt{3}}{2}\\right)^2 + \\left(\\frac{%sa}{2}\\right)^2} = \\frac{a\\sqrt{%s}}{2}$.\\\\
                             Áp dụng định lý cosin trong tam giác $MNP$: \\\\
                             $\\cos \\widehat{PMN} = \\frac{MP^2 + MN^2 - NP^2}{2 \\cdot MP \\cdot MN} = \\frac{\\frac{a^2}{4} + \\frac{%sa^2}{4} - \\frac{%sa^2}{4}}{2 \\cdot \\frac{a}{2} \\cdot \\frac{a\\sqrt{%s}}{2}} = -\\frac{1}{2\\sqrt{%s}}$.\\\\
                             Vậy $\\cos(AC; BF) = |\\cos \\widehat{PMN}| = \\frac{1}{2\\sqrt{%s}} =$ %s.'''
                           %(latex(k_val), latex(1+k_val**2), latex(k_val), latex(3+k_val**2), 
                             latex(1+k_val**2), latex(3+k_val**2), latex(1+k_val**2), 
                             latex(1+k_val**2), latex(1+k_val**2), da_text))

            # Xuất câu trắc nghiệm
            da_d = ('\\True ' + str(da_text))
            list_ans = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_ans)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

