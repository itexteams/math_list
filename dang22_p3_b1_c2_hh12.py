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


def bt_dang22_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh hình lập phương a
                a_val = random.choice([1,2,3,4,5,6,7,8])

                # Tính toán khoảng cách chính xác
                kq_exact = a_val * math.sqrt(6) / 2

                # Làm tròn đến hàng phần trăm
                kq_dec = Decimal(str(kq_exact)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # Tạo các phương án nhiễu
                s1_dec = Decimal(str(kq_exact + 0.35)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                s2_dec = Decimal(str(kq_exact - 0.45)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                s3_dec = Decimal(str(kq_exact + 1.25)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                da_d = ('\\True $%s$' % kq_str)
                da_s1 = ('$%s$' % str(s1_dec).replace('.', ','))
                da_s2 = ('$%s$' % str(s2_dec).replace('.', ','))
                da_s3 = ('$%s$' % str(s3_dec).replace('.', ','))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý text cho phương trình mặt phẳng tùy thuộc a chẵn hay lẻ để hiển thị phân số đẹp nhất
                if a_val % 2 == 0:
                    exact_str = "%s\\sqrt{6}" % (a_val // 2)
                    if a_val == 2:
                        exact_str = "\\sqrt{6}"
                    a_half_str = str(a_val // 2)
                    pt_text = "\\frac{x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow 2x + y + z - %s = 0" % (a_val // 2, a_val, a_val, a_val)
                else:
                    exact_str = "\\frac{%s\\sqrt{6}}{2}" % a_val
                    a_half_str = "\\frac{%s}{2}" % a_val
                    pt_text = "\\frac{x}{\\frac{%s}{2}} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow \\frac{2x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow 2x + y + z - %s = 0" % (a_val, a_val, a_val, a_val, a_val, a_val, a_val)

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.MNPQ$ có cạnh bằng $%s$. Gọi $E$ là trung điểm của đoạn thẳng $AB$. Khoảng cách từ điểm $P$ đến mặt phẳng $(MED)$ bằng bao nhiêu (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần trăm)?''' % (a_val))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=0.8, line width=1pt]
                \\coordinate (A) at (0,1.5);
                \\coordinate (B) at (4,1.5);
                \\coordinate (C) at (3,0);
                \\coordinate (D) at (-1,0);
                \\coordinate (M) at (0,5.5);
                \\coordinate (N) at (4,5.5);
                \\coordinate (P) at (3,4);
                \\coordinate (Q) at (-1,4);
                \\coordinate (E) at (2,1.5);
                \\draw[dashed] (A) -- (B);
                \\draw[dashed] (A) -- (D);
                \\draw[dashed] (A) -- (M);
                \\draw[dashed] (M) -- (E);
                \\draw[dashed] (E) -- (D);
                \\draw[dashed] (M) -- (D);
                \\draw (Q) -- (M) -- (N) -- (B) -- (C) -- (D) -- cycle;
                \\draw (Q) -- (P) -- (N);
                \\draw (P) -- (C);
                \\node[above left] at (A) {$A$};
                \\node[right] at (B) {$B$};
                \\node[below right] at (C) {$C$};
                \\node[below left] at (D) {$D$};
                \\node[above left] at (M) {$M$};
                \\node[above right] at (N) {$N$};
                \\node[above right] at (P) {$P$};
                \\node[left] at (Q) {$Q$};
                \\node[above] at (E) {$E$};
                \\end{tikzpicture}
                \\end{center} Chọn hệ trục tọa độ $Oxyz$ sao cho $A(0; 0; 0)$, $B(%s; 0; 0)$, $D(0; %s; 0)$, $M(0; 0; %s)$. \\\\
            Khi đó $C(%s; %s; 0)$, $P(%s; %s; %s)$. \\\\
            Vì $E$ là trung điểm của $AB$ nên $E\\left(%s; 0; 0\\right)$. \\\\
            Mặt phẳng $(MED)$ đi qua $M(0; 0; %s)$, $E\\left(%s; 0; 0\\right)$, $D(0; %s; 0)$ có phương trình theo đoạn chắn là: \\\\
            $%s$ \\\\
            Khoảng cách từ $P(%s; %s; %s)$ đến mặt phẳng $(MED)$ là: \\\\
            $d(P, (MED)) = \\frac{|2 \\cdot %s + %s + %s - %s|}{\\sqrt{2^2 + 1^2 + 1^2}} = \\frac{3 \\cdot %s}{\\sqrt{6}} = %s \\approx %s$.'''
                           % (a_val, a_val, a_val, 
                              a_val, a_val, a_val, a_val, a_val, 
                              a_half_str, 
                              a_val, a_half_str, a_val, 
                              pt_text, 
                              a_val, a_val, a_val, 
                              a_val, a_val, a_val, a_val, a_val, exact_str, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

