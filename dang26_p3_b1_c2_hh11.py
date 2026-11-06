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


def bt_dang26_p3_b1_c2_hh11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên góc CAD (alpha) từ 15 đến 75 độ, tránh 45 độ để hình không đặc biệt
                alpha = random.choice([20, 25, 30, 35, 40, 50, 55, 60])

                # Tính toán các thông số cho lời giải
                oab = 90 - alpha
                aob_val = 180 - 2 * oab

                # Góc giữa hai đường thẳng phải <= 90
                if aob_val > 90:
                    kq_val = 180 - aob_val
                else:
                    kq_val = aob_val

                da = '$' + str(kq_val) + '^\\circ$'

                # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI KHÔNG TRÙNG ĐÁP ÁN ĐÚNG ---
                s = {alpha, 90 - alpha, 2 * alpha, 180 - 2 * alpha}
                # Loại bỏ giá trị đúng nếu nó nằm trong tập s để tạo phương án nhiễu khác
                if kq_val in s:
                    s.remove(kq_val)

                # Đảm bảo có đủ phương án nhiễu
                while len(s) < 3:
                    random_val = random.randint(10, 85)
                    if random_val != kq_val:
                        s.add(random_val)

                list_s = list(s)
                random.shuffle(list_s)
                das1 = '$' + str(list_s[0]) + '^\\circ$'
                das2 = '$' + str(list_s[1]) + '^\\circ$'
                das3 = '$' + str(list_s[2]) + '^\\circ$'

                # --- BƯỚC 2: VIẾT LẠI NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                noidungcauhoi = ('''Cho hình lăng trụ $ABCD.A'B'C'D'$ có đáy là hình chữ nhật và $\\widehat{CAD} = %s^\\circ$. Số đo góc giữa hai đường thẳng $AC$ và $B'D'$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (latex(alpha)))

                # Hình vẽ TikZ
                hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, line join=round, line cap=round]|
                \coordinate (A) at (0,0);
                \coordinate (B) at (4,0);
                \coordinate (C) at (5,1.5);
                \coordinate (D) at (1,1.5);
                \coordinate (A1) at (0,4);
                \coordinate (B1) at (4,4);
                \coordinate (C1) at (5,5.5);
                \coordinate (D1) at (1,5.5);
                \coordinate (O) at (2.5,0.75);
                \draw (A1)--(B1)--(C1)--(D1)--cycle;
                \draw (A1)--(A) (B1)--(B) (C1)--(C);
                \draw[dashed] (D1)--(D) (D)--(A) (D)--(C) (A)--(C) (B)--(D);
                \draw (A)--(B)--(C);
                \node[left] at (A){$A$}; \node[right] at (B){$B$}; \node[right] at (C){$C$}; \node[left] at (D){$D$};
                \node[left] at (A1){$A'$}; \node[right] at (B1){$B'$}; \node[right] at (C1){$C'$}; \node[left] at (D1){$D'$};
                \node[below] at (O){$O$};
            \end{tikzpicture}
            \end{center}'''

                loigiai = ('''Ta có $BD // B'D' \\Rightarrow (AC; B'D') = (AC; BD)$. \\\\
                             Gọi $O = AC \\cap BD$. Vì $ABCD$ là hình chữ nhật nên $O$ là trung điểm của mỗi đường chéo, suy ra $OA = OB$. \\\\
                             Xét tam giác $ABC$ vuông tại $B$, ta có $\\widehat{CAB} = 90^\\circ - \\widehat{CAD} = 90^\\circ - %s^\\circ = %s^\\circ$. \\\\
                             Vì $OA = OB$ nên tam giác $OAB$ cân tại $O$, suy ra $\\widehat{OBA} = \\widehat{OAB} = %s^\\circ$. \\\\
                             Trong tam giác $OAB$, ta có $\\widehat{AOB} = 180^\\circ - (\\widehat{OAB} + \\widehat{OBA}) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$. \\\\
                             Góc giữa hai đường thẳng $AC$ và $BD$ là góc không tù, do đó: \\\\
                             Nếu $\\widehat{AOB} \\le 90^\\circ$ thì $(AC; BD) = \\widehat{AOB} = %s^\\circ$. \\\\
                             Nếu $\\widehat{AOB} > 90^\\circ$ thì $(AC; BD) = 180^\\circ - \\widehat{AOB} = 180^\\circ - %s^\\circ = %s^\\circ$. \\\\
                             Vậy $(AC, B'D') = %s^\\circ$.'''
                           % (latex(alpha), latex(oab), latex(oab), latex(oab), latex(oab), latex(aob_val), 
                              latex(aob_val), latex(aob_val), latex(kq_val), latex(kq_val)))
                h1=kq_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)#Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + hinh_ve + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

