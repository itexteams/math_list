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


def bt_dang5_p3_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn giá trị ngẫu nhiên cho cạnh a (nên chọn số chẵn để tính toán đẹp)
            lis_a = [4, 6, 8, 10, 12, 14, 16]
            a_val = random.choice(lis_a)

            # Tính toán các giá trị trung gian
            # BE = CE = a * sqrt(3) / 2
            be_val = Rational(a_val, 2) * sqrt(3)
            # BC = a
            bc_val = a_val
            # BF = a / 2
            bf_val = Rational(a_val, 2)
            # EF = sqrt(BE^2 - BF^2) = a * sqrt(2) / 2
            ef_val = Rational(a_val, 2) * sqrt(2)

            # Diện tích thiết diện S = 1/2 * EF * BC = (a^2 * sqrt(2)) / 4
            s_val = Rational(a_val**2, 4) * sqrt(2)

            # Tính giá trị thập phân để làm tròn theo yêu cầu (hàng phần chục)
            s_decimal = Decimal(float(s_val.evalf())).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq = str(s_decimal).replace('.', ',')

            # Tạo các phương án nhiễu
            da_dung = '$%s$' % (latex(s_val))
            s1 = '$%s$' % (latex(Rational(a_val**2, 4) * sqrt(3)))
            s2 = '$%s$' % (latex(a_val**2 / 4))
            s3 = '$%s$' % (latex(a_val**2 / 3))
            s4 = '$%s$' % (latex(Rational(a_val**2, 2) * sqrt(2)))

            list_s = [s1, s2, s3, s4]
            random.shuffle(list_s)

            das1 = list_s[0]
            das2 = list_s[1]
            das3 = list_s[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho tứ diện đều $ABCD$ cạnh $a = %s$, gọi $(P)$ là mặt phẳng qua $B$ và vuông góc với $AD$. Thiết diện của $(P)$ và hình chóp có diện tích bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                             % (latex(a_val)))

            # Các đáp án theo cấu trúc \True
            da_d = ('\\True ' + str(da_dung))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Vẽ hình bằng TikZ (giữ nguyên tỷ lệ và nét vẽ 1pt)
            ve_hinh = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, line width=1pt]
                \coordinate (B) at (0,0);
                \coordinate (D) at (5,0);
                \coordinate (C) at (1.5,-1.8);
                \coordinate (A) at (2.5,4.5);
                \coordinate (E) at ($(A)!0.5!(D)$);
                \coordinate (F) at ($(B)!0.5!(C)$);
                \draw[dashed] (B) -- (D);
                \draw[dashed] (B) -- (E);
                \draw[dashed] (E) -- (F);
                \draw (A) -- (B) -- (C) -- (A);
                \draw (A) -- (D) -- (C);
                \draw (E) -- (C);
                \fill (A)  node[above] {$A$};
                \fill (B)  node[left] {$B$};
                \fill (C)  node[below] {$C$};
                \fill (D)  node[right] {$D$};
                \fill (E)  node[right] {$E$};
                \fill (F)  node[left] {$F$};
            \end{tikzpicture}
            \end{center}'''

            # Nội dung lời giải chi tiết
            loigiai = (ve_hinh + '''Gọi $E$ là trung điểm $AD$. \\\\
            Do tam giác $ABD$ đều nên $BE \\perp AD$ (1). \\\\
            Do tam giác $ACD$ đều nên $CE \\perp AD$ (2). \\\\
            Từ (1) và (2) suy ra: $AD \\perp \\left( BCE \\right) $. \\\\
            $\\Rightarrow$ Thiết diện là tam giác $BCE$. Gọi $F$ là trung điểm của $BC$. \\\\
            Ta có $BE = CE = \\frac{%s\\sqrt{3}}{2} = %s$. \\\\
            $EF = \\sqrt{BE^2 - BF^2} = \\sqrt{\\left( %s \\right)^2 - \\left( %s \\right)^2} = %s$. \\\\
            Diện tích thiết diện là: \\\\
            $S = \\frac{1}{2} EF \\cdot BC = \\frac{1}{2} \\cdot %s \\cdot %s = %s \\approx %s$.'''
                       % (latex(a_val), latex(be_val), latex(be_val), latex(bf_val), latex(ef_val),
                          latex(ef_val), latex(bc_val), latex(s_val), kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm (không dùng raw string r'' trong phần content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

