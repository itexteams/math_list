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


def bt_dang14_p3_b2_c7_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        L_val = choice([8, 10, 12, 15])
        v_val = choice([1, 2])
        # Chọn t_val sao cho v_val * t_val < L_val
        max_t = (L_val - 1) // v_val
        t_val = choice([t for t in range(2, max_t + 1) if t * v_val < L_val])

        # Tính toán chính xác
        mau = L_val + v_val * t_val
        # S'(t) = - 2 * v_val * L_val^4 / (mau^3)
        toc_do_giam = Rational(2 * v_val * (L_val**4), mau**3)

        # Làm tròn đến hàng phần trăm
        number = Decimal(str(float(toc_do_giam)))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Vẽ hình TikZ 100% như ảnh mẫu
        hinhve = '''\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4,0);
    \\coordinate (C) at (4,4);
    \\coordinate (D) at (0,4);
    \\coordinate (Q) at (4,1.2);
    \\coordinate (M) at (0,1.0);
    \\coordinate (P) at (3.0,4);
    \\coordinate (N) at (3.0,1.0);
    \\draw[->, line width=1pt] (0,0) -- (4.8,0) node[below] {$x$};
    \\draw[->, line width=1pt] (0,0) -- (0,4.8) node[left] {$y$};
    \\draw[line width=1pt, dashed] (D)--(C)--(B);
    \\draw[line width=1pt, dashed] (A)--(Q);
    \\fill[yellow!15] (M)--(N)--(P)--(D)--cycle;
    \\draw[line width=1pt] (M)--(N)--(P)--(D)--cycle;
    \\draw[->, line width=1pt] (B) -- (Q);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[below right] {$N$};
    \\fill (P) circle (1pt) node[above] {$P$};
    \\fill (Q) circle (1pt) node[right] {$Q$};
    \\end{tikzpicture}'''

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Cho hình vuông $ABCD$ có cạnh bằng $%s\\text{ m}$, điểm $Q$ chuyển động thẳng đều từ vị trí $B$ đến vị trí $C$ với tốc độ $%s\\text{ m/s}$ (thời điểm $t = 0$ giây được tính khi $Q$ xuất phát từ $B$). Với mỗi vị trí của $Q$, luôn tồn tại hình vuông $DMNP$ với $M$ thuộc đoạn $AD$, $N$ thuộc $AQ$ và $P$ thuộc đoạn $CD$. Hỏi tại thời điểm $t = %s$ giây thì diện tích hình vuông $DMNP$ giảm với tốc độ bao nhiêu $\\text{m}^2/\\text{s}$? (Làm tròn kết quả đến hàng phần chục).}{%s}'''
                         % (str(L_val), str(v_val), str(t_val), hinhve))



        # Nội dung lời giải
        loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O$ trùng với đỉnh $A(0;0)$, tia $Ox$ chứa cạnh $AB$, tia $Oy$ chứa cạnh $AD$. \\\\
                   Khi đó tọa độ các đỉnh của hình vuông là: $A(0;0)$, $B(%s;0)$, $C(%s;%s)$, $D(0;%s)$. \\\\
                   Tại thời điểm $t$ giây, quãng đường điểm $Q$ đi được từ $B$ là $BQ = %s \\cdot t = %st\\text{ (m)}$. \\\\
                   Do $Q$ chuyển động trên cạnh $BC$ nên tọa độ của điểm $Q$ là $Q(%s;%st)$. \\\\
                   Phương trình đường thẳng $AQ$ đi qua gốc tọa độ $A(0;0)$ và $Q(%s;%st)$ là: \\\\
                   $y = \\dfrac{%st}{%s}x = \\dfrac{%st}{%s}x$. \\\\
                   Gọi $s$ là độ dài cạnh của hình vuông $DMNP$ ($0 < s < %s$). \\\\
                   Vì $M \\in AD$ và $P \\in CD$ nên: \\\\
                   + Điểm $M$ có tọa độ $M(0; %s - s)$. \\\\
                   + Điểm $P$ có tọa độ $P(s; %s)$. \\\\
                   Suy ra điểm $N$ có tọa độ là $N(s; %s - s)$. \\\\
                   Mặt khác, điểm $N$ thuộc đoạn thẳng $AQ$ nên tọa độ điểm $N$ thỏa mãn phương trình đường thẳng $AQ$: \\\\
                   $%s - s = \\dfrac{%st}{%s} \\cdot s \\Leftrightarrow s \\left(1 + \\dfrac{%st}{%s}\\right) = %s \\Leftrightarrow s \\left(\\dfrac{%s + %st}{%s}\\right) = %s \\Leftrightarrow s(t) = \\dfrac{%s}{%s + %st}$. \\\\
                   Diện tích của hình vuông $DMNP$ tại thời điểm $t$ là: \\\\
                   $S(t) = s^2(t) = \\left(\\dfrac{%s}{%s + %st}\\right)^2 = \\dfrac{%s}{(%s + %st)^2}$. \\\\
                   Tốc độ thay đổi diện tích hình vuông $DMNP$ theo thời gian được xác định bởi đạo hàm $S'(t)$: \\\\
                   $S'(t) = -\\dfrac{2 \\cdot %s \\cdot (%s + %st) \\cdot %s}{(%s + %st)^4} = -\\dfrac{%s}{(%s + %st)^3}$. \\\\
                   Tại thời điểm $t = %s$ giây: \\\\
                   $S'(%s) = -\\dfrac{%s}{(%s + %s \\cdot %s)^3} = -\\dfrac{%s}{%s^3} \\approx -%s\\text{ (m$^2$/s)}$. \\\\
                   Dấu âm biểu thị diện tích hình vuông đang giảm. Vậy tại thời điểm $t = %s$ giây, diện tích hình vuông $DMNP$ giảm với tốc độ khoảng $%s\\text{ m}^2/\\text{s}$.'''
                   % (
                      str(L_val), str(L_val), str(L_val), str(L_val),
                      str(v_val), str(v_val) if v_val != 1 else "",
                      str(L_val), str(v_val) if v_val != 1 else "",
                      str(L_val), str(v_val) if v_val != 1 else "",
                      str(v_val) if v_val != 1 else "", str(L_val),
                      str(v_val) if v_val != 1 else "", str(L_val),
                      str(L_val),
                      str(L_val),
                      str(L_val),
                      str(L_val),
                      str(L_val), str(v_val) if v_val != 1 else "", str(L_val),
                      str(v_val) if v_val != 1 else "", str(L_val), str(L_val),
                      str(L_val), str(v_val) if v_val != 1 else "", str(L_val), str(L_val),
                      str(L_val**2), str(L_val), str(v_val) if v_val != 1 else "",
                      str(L_val**2), str(L_val), str(v_val) if v_val != 1 else "",
                      str(L_val**4), str(L_val), str(v_val) if v_val != 1 else "",
                      str(L_val**4), str(L_val), str(v_val) if v_val != 1 else "", str(v_val), str(L_val), str(v_val) if v_val != 1 else "",
                      str(2 * v_val * (L_val**4)), str(L_val), str(v_val) if v_val != 1 else "",
                      str(t_val),
                      str(t_val),
                      str(2 * v_val * (L_val**4)), str(L_val), str(v_val), str(t_val),
                      str(2 * v_val * (L_val**4)), str(mau),
                      str(kq_str),
                      str(t_val), str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')
    return content

