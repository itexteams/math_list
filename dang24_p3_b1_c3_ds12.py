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


def bt_dang24_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                t1 = random.choice([2, 3, 4])
                t2 = random.choice([6, 7, 8])

                # Giá trị gia tốc tại t1 và t2 (dạng căn thức để giống mẫu)
                val_a1 = random.choice([2, 3, 5]) 
                val_a2 = random.choice([6, 7, 8, 10])
                a1_sym = sqrt(val_a1)
                a2_sym = sqrt(val_a2)

                # Vận tốc ban đầu tại t=0
                v0 = random.randint(1, 5) 

                t = symbols('t')

                f1 = (a1_sym / t1) * t
                # v1(t) = integrate(f1) + v0
                v1_func = integrate(f1, t) + v0
                v1_at_t1 = v1_func.subs(t, t1)

                # --- Đoạn 2: t in [t1, t2] ---
                # Đường thẳng qua (t1, sqrt(val_a1)) và (t2, sqrt(val_a2))
                m2 = (a2_sym - a1_sym) / (t2 - t1)
                n2 = a1_sym - m2 * t1
                f2 = m2 * t + n2


                v2_pre = integrate(f2, t)
                C_val = simplify(v1_at_t1 - v2_pre.subs(t, t1))
                v2_func = v2_pre + C_val

                # Kết quả cuối cùng tại t2
                v_final_val = float(v2_func.subs(t, t2))

                # Làm tròn đến hàng phần mười
                kq_decimal = Decimal(str(v_final_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s(m/s)$' % kq_str

                # Bước 4: Các phương án sai
                s_wrong = set()
                while len(s_wrong) < 3:
                    sai_offset = random.choice([-2.4, -1.5, 0.7, 1.2, 2.5, 3.1])
                    sai_val = float(kq_decimal) + sai_offset
                    if sai_val > 0:
                        sw_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if sw_str != kq_str:
                            s_wrong.add('$%s(m/s)$' % sw_str)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Tạo mã TikZ cho hình vẽ
                tikz_code = (r'''\begin{center}
                \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \draw[->] (0,0) -- (%s,0) node[below] {$t$};
                    \draw[->] (0,0) -- (0,%s) node[left] {$a(t)$};
                    \draw[blue, thick] (0,0) -- (%s,%s) -- (%s,%s);
                    \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
                    \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
                    \node[below] at (%s,0) {$%s$};
                    \node[below] at (%s,0) {$%s$};
                    \node[below left] at (0,%s) {$\sqrt{%s}$};
                    \node[above left] at (0,%s) {$\sqrt{%s}$};
                    \node[below left] at (0,0) {$O$};
                \end{tikzpicture}
                \end{center}''' % (t2+1, 4, t1, math.sqrt(val_a1), t2, math.sqrt(val_a2), 
                                    t1, t1, math.sqrt(val_a1), math.sqrt(val_a1),
                                    t2, t2, math.sqrt(val_a2), math.sqrt(val_a2),
                                    t1, t1, t2, t2, math.sqrt(val_a1), val_a1, math.sqrt(val_a2), val_a2))

                # Câu hỏi
                noidungcauhoi = (r'''Một vật chuyển động với hàm số gia tốc là $a(t)$. Biết rằng đồ thị hàm số $a(t)$ trên đoạn $[0;%s]$ được cho như hình dưới đây và vận tốc tại thời điểm $t=0$ là $v(0)=%s$(m/s). 
                %s
                Tại thời điểm $t=%s$ giây, vận tốc của vật là bao nhiêu? (làm tròn kết quả đến chữ số thập phân thứ nhất).''' 
                                 % (t2, v0, tikz_code, t2))

                # Nội dung lời giải
                loigiai = (r'''Từ đồ thị ta xác định hàm gia tốc $a(t)$ trên từng đoạn: \\
                             $a(t) = \begin{cases} %s, & 0 \le t \le %s \\ %s, & %s \le t \le %s \end{cases}$. \\
                             Biết $v(0)=%s$(m/s), ta tính hàm vận tốc $v(t) = \int a(t) \text{d}t$: \\
                             $v(t) = \begin{cases} %s, & 0 \le t \le %s \\ %s + C, & %s \le t \le %s \end{cases}$. \\
                             Vì vận tốc là hàm số liên tục tại $t=%s$ nên: \\
                             $\lim_{t \to %s^-} v(t) = \lim_{t \to %s^+} v(t) \Leftrightarrow %s = %s + C \Rightarrow C = %s$. \\
                             Khi đó tại thời điểm $t=%s$, vận tốc vật là: \\
                             $v(%s) = \left( %s \right) \Big|_{t=%s} + %s \approx %s$ (m/s).'''
                           % (latex(f1), t1, latex(f2), t1, t2,
                              v0, latex(v1_func), t1, latex(v2_pre), t1, t2,
                              t1, t1, t1, latex(v1_at_t1), latex(v2_pre.subs(t, t1)), latex(C_val),
                              t2, t2, latex(v2_pre), t2, latex(C_val), kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content  

