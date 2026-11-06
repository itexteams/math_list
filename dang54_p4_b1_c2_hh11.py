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


def bt_dang54_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Sử dụng số nguyên cho các hệ số
            m = random.choice([2, 4, 6]) 
            n = random.choice([1, 2, 3])
            goc_val = random.choice([30, 45, 60])

            # KHẮC PHỤC: Khai báo a là số dương để sqrt(a**2) = a
            a = symbols('a', positive=True)

            # Tính toán hoàn toàn bằng symbolic (Sympy)
            AB_val = m * a
            BC_val = n * a
            HB_val = Rational(m, 2) * a 

            # AC = sqrt(AB^2 + BC^2) - Tự động rút gọn a ra ngoài căn
            AC_expr = simplify(sqrt(AB_val**2 + BC_val**2))

            # HC = sqrt(HB^2 + BC^2)
            HC_expr = simplify(sqrt(HB_val**2 + BC_val**2))

            # SH = HC * tan(goc)
            goc_rad = Rational(goc_val, 180) * pi
            SH_expr = simplify(HC_expr * tan(goc_rad))

            # SB = sqrt(SH^2 + HB^2)
            SB_expr = simplify(sqrt(SH_expr**2 + HB_val**2))

            # Tích vô hướng: vec(HB).vec(AB) = HB * AB
            tich_vh = simplify(HB_val * AB_val)

            # Cosin góc giữa SB và AC (a sẽ tự triệt tiêu ở tử và mẫu)
            cos_phi = simplify(tich_vh / (SB_expr * AC_expr))

            # =============================================================================
            # BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI
            # =============================================================================

            da_dung = '$%s$' % latex(cos_phi)

            s = []
            options_formulas = [
                tich_vh / (SH_expr * AC_expr), 
                tich_vh / (HC_expr * AC_expr), 
                simplify(Rational(m, 4) * m * a**2 / (SB_expr * AC_expr)), 
                simplify(sqrt(1 - cos_phi**2)), 
                simplify(cos_phi * Rational(1, 2)),
                simplify(cos_phi * sqrt(2))
            ]

            for f in options_formulas:
                val = '$%s$' % latex(simplify(f))
                if val != da_dung and val not in s:
                    s.append(val)

            while len(s) < 3:
                s.append('$%s$' % latex(cos_phi + Rational(random.randint(1,5), 10)))

            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # =============================================================================
            # BƯỚC 2: VIẾT LẠI THEO MẪU CODE PYTHON
            # =============================================================================

            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật, $AB = %s a$, $BC = %s a$. Hình chiếu vuông góc $H$ của đỉnh $S$ trên mặt phẳng đáy là trung điểm của cạnh $AB$, góc giữa đường thẳng $SC$ và mặt phẳng đáy bằng $%s^\\circ$. Tính cosin góc giữa hai đường thẳng $SB$ và $AC$.'''
                            % (latex(m), latex(n), latex(goc_val)))

            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
                \coordinate (B) at (0,0);
                \coordinate (C) at (4,0);
                \coordinate (A) at (1.5,1.2);
                \coordinate (D) at ($(A)+(C)-(B)$);
                \coordinate (H) at ($(A)!0.5!(B)$);
                \coordinate (S) at ($(H)+(0,3.5)$);
                \draw (S)--(B)--(C)--(S) (S)--(D)--(C);
                \draw[dashed] (S)--(A)--(B) (A)--(D) (S)--(H)--(C) (A)--(C);
                \filldraw (S)  node[above] {$S$}
                          (A)  node[above left] {$A$}
                          (B)  node[below left] {$B$}
                          (C)  node[below right] {$C$}
                          (D)  node[right] {$D$}
                          (H)  node[left] {$H$};
            \end{tikzpicture}
            \end{center}'''

            loigiai = ('''%s
            Vì $SH \\perp (ABCD)$ nên $HC$ là hình chiếu của $SC$ lên mặt đáy. \\\\
            Góc giữa $SC$ và đáy là $\\widehat{SCH} = %s^\\circ$. \\\\
            Ta có $HB = \\frac{AB}{2} = \\frac{%s a}{2} = %s a$. \\\\
            Trong $\\triangle HBC$ vuông tại $B$: $CH = \\sqrt{HB^2 + BC^2} = \\sqrt{(%s a)^2 + (%s a)^2} = %s$. \\\\
            Trong $\\triangle SHC$ vuông tại $H$: $SH = CH \\cdot \\tan %s^\\circ = %s \\cdot %s = %s$. \\\\
            Trong $\\triangle SHB$ vuông tại $H$: $SB = \\sqrt{SH^2 + HB^2} = \\sqrt{(%s)^2 + (%s a)^2} = %s$. \\\\
            Trong $\\triangle ABC$ vuông tại $B$: $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{(%s a)^2 + (%s a)^2} = %s$. \\\\
            Ta có $\\cos(SB, AC) = \\frac{|\\vec{SB} \\cdot \\vec{AC}|}{SB \\cdot AC}$. \\\\
            Mà $\\vec{SB} \\cdot \\vec{AC} = (\\vec{SH} + \\vec{HB})(\\vec{AB} + \\vec{BC}) = \\vec{SH}\\cdot\\vec{AB} + \\vec{SH}\\cdot\\vec{BC} + \\vec{HB}\\cdot\\vec{AB} + \\vec{HB}\\cdot\\vec{BC}$. \\\\
            Do $SH \\perp (ABCD)$ và $HB \\perp BC$ nên: \\\\
            $\\vec{SB} \\cdot \\vec{AC} = \\vec{HB} \\cdot \\vec{AB} = HB \\cdot AB = %s a \\cdot %s a = %s a^2$. \\\\
            Suy ra $\\cos(SB, AC) = \\frac{%s a^2}{%s \\cdot %s} = %s$.'''
                      % (tikz_code, latex(goc_val),
                         latex(m), latex(Rational(m, 2)),
                         latex(Rational(m, 2)), latex(n), latex(HC_expr),
                         latex(goc_val), latex(HC_expr), latex(simplify(tan(goc_rad))), latex(SH_expr),
                         latex(SH_expr), latex(Rational(m, 2)), latex(SB_expr),
                         latex(m), latex(n), latex(AC_expr),
                         latex(Rational(m, 2)), latex(m), latex(simplify(tich_vh/a**2)),
                         latex(simplify(tich_vh/a**2)), latex(SB_expr), latex(AC_expr), latex(cos_phi)
                         ))

            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

