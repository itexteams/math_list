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


def bt_dang45_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Ta sẽ random tỉ lệ k = D'M / D'D. Trong hình k = 1/2.
            lis_k = [Rational(1, 2), Rational(1, 3), Rational(2, 3), Rational(1, 4)]
            k = random.choice(lis_k)

            # Tính toán các đại lượng dựa trên cạnh a (giả sử a=1 để tính tỉ số)
            # B'C = sqrt(2)
            # B'N = sqrt(1 + k^2) với N thuộc AA' sao cho A'N = D'M
            # NC^2 = AC^2 + AN^2 = 2 + (1-k)^2
            b_prime_c_sq = Rational(2, 1)
            b_prime_n_sq = 1 + k**2
            nc_sq = 2 + (1-k)**2

            # Cosin theo định lý hàm số cos: cos = (B'N^2 + B'C^2 - NC^2) / (2 * B'N * B'C)
            # Tử số: (1 + k^2) + 2 - (2 + (1-k)^2) = 1 + k^2 - (1 - 2k + k^2) = 2k
            tu_so = 2*k
            mau_so = 2 * sqrt(b_prime_n_sq) * sqrt(b_prime_c_sq)
            cos_val = tu_so / mau_so
            cos_val = sp.simplify(cos_val)

            # Tạo đáp án đúng
            da_dung = '$%s$' % latex(cos_val)

            # Tạo các đáp án sai ngẫu nhiên
            s = [
                '$%s$' % latex(sp.simplify(Rational(1, 2) * cos_val)),
                '$%s$' % latex(sp.simplify(sqrt(3) * cos_val)),
                '$%s$' % latex(sp.simplify(cos_val / 2)),
                '$%s$' % latex(sp.simplify(Rational(2, 3) * sqrt(2))),
                '$1/3$', '$\\sqrt{2}/2$', '$\\sqrt{3}/3$', '$2/5$'
            ]
            random.shuffle(s)
            # Lọc bỏ đáp án trùng với đáp án đúng
            s = [x for x in s if x != da_dung]
            das1, das2, das3 = s[:3]

            # Nội dung câu hỏi
            ti_le_str = ""
            if k == Rational(1, 2):
                ti_le_str = "trung điểm"
            else:
                ti_le_str = "điểm thỏa mãn $D'M = \\frac{%s}{%s} DD'$" % (latex(k.p), latex(k.q))

            noidungcauhoi = (r"Cho hình lập phương $ABCD.A'B'C'D'$. Gọi $M$ là %s của cạnh $DD'$. Tính cosin của góc giữa hai đường thẳng $B'C$ và $C'M$." % ti_le_str)

            # Vẽ hình TikZ
            # Định nghĩa tọa độ các đỉnh
            tikz_code = r"""\begin{tikzpicture}[scale=2, line join=round, line cap=round]
                \coordinate (A') at (0,0);
                \coordinate (B') at (1.5,-0.4);
                \coordinate (C') at (2.5,0.2);
                \coordinate (D') at (1,0.6);
                \coordinate (A) at (0,1.5);
                \coordinate (B) at (1.5,1.1);
                \coordinate (C) at (2.5,1.7);
                \coordinate (D) at (1,2.1);
                \coordinate (M) at ($(D')!%s!(D)$);
                \coordinate (N) at ($(A')!%s!(A)$);
                \draw[dashed] (A')--(D') (C')--(D') (D')--(D) (A')--(N) (C')--(M);
                \draw (A')--(B')--(C')--(C)--(B)--(A)--cycle (B')--(N);
                \draw (B')--(B) (C')--(C) (A)--(D)--(C) (B')--(C);
                \draw (B')--(C) ;
                \draw[dashed] (B')--(N);
                \foreach \p/\pos in {A/left, B/below, C/right, D/above, A'/left, B'/below, C'/right, D'/above, M/right, N/left}
                    \fill (\p) node[\pos] {$\p$};
            \end{tikzpicture}""" % (latex(float(k)), latex(float(k)))

            # Lời giải chi tiết
            loigiai = (r"""Giả sử hình lập phương có cạnh bằng $a$. \\
            Kẻ $B'N$ song song với $C'M$ với $N$ thuộc cạnh $AA'$ sao cho $A'N = D'M = %sa$. \\
            Khi đó góc giữa $(B'C; C'M) = (B'C; B'N) = \widehat{NB'C}$ (hoặc bù với góc này). \\
            Ta có: \\
            $B'C = \sqrt{B'C'^2 + C'C^2} = a\sqrt{2}$. \\
            $B'N = \sqrt{A'B'^2 + A'N^2} = \sqrt{a^2 + (%sa)^2} = %sa$. \\
            $NC = \sqrt{AC^2 + AN^2} = \sqrt{(a\sqrt{2})^2 + (a - %sa)^2} = \sqrt{2a^2 + (%sa)^2} = %sa$. \\
            Áp dụng định lý hàm số côsin trong $\triangle B'NC$: \\
            $\cos \widehat{NB'C} = \frac{B'N^2 + B'C^2 - NC^2}{2 \cdot B'N \cdot B'C} = \frac{(%s a^2) + (2a^2) - (%s a^2)}{2 \cdot %s a \cdot a\sqrt{2}} = %s$. \\
            Vậy giá trị cosin cần tìm là $%s$.""" 
            % (latex(k), latex(k), latex(sqrt(b_prime_n_sq)), latex(k), latex(1-k), latex(sqrt(nc_sq)),
               latex(b_prime_n_sq), latex(nc_sq), latex(sqrt(b_prime_n_sq)), latex(cos_val), latex(cos_val)))

            # Xuất nội dung theo mẫu
            list_1 = ['\\True ' + str(da_dung), str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{''\\begin{center}\n' + tikz_code + '\n\\end{center}\n' +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

