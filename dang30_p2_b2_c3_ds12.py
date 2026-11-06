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


def bt_dang30_p2_b2_c3_ds12(self):
            # Khai báo biến
            def fmt_dec(val):
                """Hàm định dạng số thập phân sử dụng dấu phẩy"""
                s = f"{float(val):.4f}".rstrip('0').rstrip('.')
                return s.replace('.', ',')

            # Khai báo biến
            x = symbols('x')

            # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn yêu cầu bài toán
            while True:
                # Chọn v0 (m/s) sao cho nhân 3.6 ra số nguyên chẵn (vd: 15, 20, 25)
                v0_ms = random.choice([15, 20, 25, 30])
                # Chọn v_gh (m/s) nhỏ hơn v0
                vgh_ms = random.choice([10, 15, 20])
                if vgh_ms >= v0_ms: 
                    continue

                # Giai đoạn 1: Hãm phanh đạt tốc độ giới hạn
                t1 = random.choice([2, 4, 5, 8])
                a = sp.Rational(vgh_ms - v0_ms, t1)
                # Đảm bảo gia tốc a ra số thập phân đẹp
                if a.q not in [1, 2, 4, 5, 8]: 
                    continue

                S1_val = sp.Rational((v0_ms + vgh_ms) * t1, 2)
                if S1_val.q != 1: 
                    continue
                S1 = int(S1_val)

                # Giai đoạn 2: Giữ nguyên vận tốc giới hạn
                t2 = random.choice([5, 8, 10, 12, 15])
                S2 = vgh_ms * t2

                # Giai đoạn 3: Giảm tốc đến khi dừng
                T3 = random.choice([3, 4, 5, 6, 8, 10])
                S3_val = sp.Rational(2 * vgh_ms * T3, 3)
                if S3_val.q != 1: 
                    continue
                S3 = int(S3_val)

                # Tổng quãng đường
                S_AB = S1 + S2 + S3

                # Các hằng số giai đoạn 3
                b = v0_ms
                d = vgh_ms
                c = sp.Rational(-d, T3**2)

                # Tính vận tốc tại thời điểm t_ask ngẫu nhiên
                dt = random.randint(1, T3 - 1)
                t_ask = t1 + t2 + dt
                v_ask = c * dt**2 + d
                if v_ask.q not in [1, 2, 4, 5, 8]: 
                    continue

                # Vận tốc theo km/h
                v0_kmh = int(v0_ms * 3.6)
                vgh_kmh = int(vgh_ms * 3.6)

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một ô tô đang di chuyển với tốc độ %s (km/h) tại vị trí $A$ thì tài xế quan sát thấy biển báo giới hạn tốc độ nên đạp phanh để giảm tốc và hàm vận tốc được tuân theo quy luật $v(t)=at+b$ (m/s). Sau %s giây hãm phanh, xe đi được quãng đường là %s m và vận tốc lúc này vừa đúng bằng tốc độ giới hạn cho phép. Tài xế tiếp tục giữ nguyên tốc độ giới hạn này đi tiếp trong %s giây để đi qua hết khu vực này. Sau đó, xe tiếp tục giảm tốc theo quy luật $v(t)=ct^2+d$ (m/s) và dừng hẳn tại $B$. Biết tổng quãng đường từ $A$ đến $B$ bằng %s m.'''
                             % (v0_kmh, t1, S1, t2, S_AB))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                # Mệnh đề a)
                a_true = "\\True Biển báo quy định tốc độ giới hạn tối đa là %s (km/h)" % (vgh_kmh)
                a_false = "Biển báo quy định tốc độ giới hạn tối đa là %s (km/h)" % (vgh_kmh + random.choice([5, 10, -5]))
                nb_da_1 = random.choice([a_true, a_false])
                ans_a = "đúng" if "\\True" in nb_da_1 else "sai"

                # Mệnh đề b)
                b_true = "\\True $a = %s$" % (fmt_dec(a))
                b_false = "$a = %s$" % (fmt_dec(a + random.choice([0.25, -0.25, 0.5, -0.5])))
                th_da_1 = random.choice([b_true, b_false])
                ans_b = "đúng" if "\\True" in th_da_1 else "sai"

                # Mệnh đề c)
                c_true = "\\True Quãng đường xe chạy với tốc độ không đổi là %s m" % (S2)
                c_false = "Quãng đường xe chạy với tốc độ không đổi là %s m" % (S2 + random.choice([-20, 20, 50, -50]))
                vd_da_1 = random.choice([c_true, c_false])
                ans_c = "đúng" if "\\True" in vd_da_1 else "sai"

                # Mệnh đề d)
                d_true = "\\True Tại thời điểm $t = %s$ giây tính từ $A$ thì vận tốc của xe là %s (m/s)" % (t_ask, fmt_dec(v_ask))
                d_false = "Tại thời điểm $t = %s$ giây tính từ $A$ thì vận tốc của xe là %s (m/s)" % (t_ask, fmt_dec(v_ask + random.choice([1, -1, 1.25, -1.25])))
                vdc_da_1 = random.choice([d_true, d_false])
                ans_d = "đúng" if "\\True" in vdc_da_1 else "sai"

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vận tốc ban đầu tại $A$ là $v_0 = %s$ (km/h) $= %s$ (m/s) và quãng đường $AB = %s$ m.\\\\
            Tại $t=0$, xe bắt đầu hãm phanh nên $v(0)=%s \\Rightarrow a \\cdot 0 + b = %s \\Rightarrow b=%s$.\\\\
            Quãng đường đi được trong %s giây là %s m: $S_1 = \\int\\limits_0^{%s} (at+%s)\\mathrm{d}t = %s \\Leftrightarrow a=%s$.\\\\
            Vận tốc giới hạn tại thời điểm kết thúc giai đoạn 1 là $t=%s$ nên $v_{gh}=v(%s)=%s \\cdot %s + %s = %s$ (m/s).\\\\
            Vậy vận tốc giới hạn là: $v_{gh}=%s \\cdot 3,6 = %s$ (km/h) nên mệnh đề a) %s.'''
                % (v0_kmh, v0_ms, S_AB, v0_ms, v0_ms, v0_ms, t1, S1, t1, v0_ms, S1, fmt_dec(a), t1, t1, fmt_dec(a), t1, v0_ms, vgh_ms, vgh_ms, vgh_kmh, ans_a))

            loigiai_th_1 = ('''Theo câu a) nên $a=%s$ nên mệnh đề b) %s.'''
                % (fmt_dec(a), ans_b))

            loigiai_vd_1 = ('''Xe giữ nguyên vận tốc giới hạn $v_2=%s$ (m/s) nên quãng đường đi được trong giai đoạn 2 là:\\\\
            $S_2 = v_2 \\cdot t = %s \\cdot %s = %s$ (m) nên mệnh đề c) %s.'''
                % (vgh_ms, vgh_ms, t2, S2, ans_c))

            loigiai_vdc_1 = ('''Quãng đường còn lại cho giai đoạn 3: $S_3 = S_{AB} - S_1 - S_2 = %s - %s - %s = %s$ (m).\\\\
            Tại thời điểm bắt đầu giai đoạn 3: $v_3(0) = c \\cdot 0^2 + d = %s \\Rightarrow d=%s$.\\\\
            Tại thời điểm $T$ thì xe dừng hẳn nên vận tốc bằng 0 $\\Leftrightarrow v_3(T) = cT^2 + %s = 0 \\Rightarrow cT^2 = -%s$ (*).\\\\
            Quãng đường đi được là %s m nên $S_3 = \\int\\limits_0^T (ct^2+%s)\\mathrm{d}t = %s$ kết hợp (*) suy ra $T=%s$ (giây).\\\\
            Thay $T=%s$ vào (*) suy ra $c=%s$.\\\\
            Tại thời điểm $t=%s$ giây tương ứng với giây thứ %s của giai đoạn 3 nên ta thay vào phương trình ta được $v_3(t) = %s \\cdot %s^2 + %s = %s$ (m/s) nên mệnh đề d) %s.'''
                % (S_AB, S1, S2, S3, vgh_ms, vgh_ms, vgh_ms, vgh_ms, S3, vgh_ms, S3, T3, T3, latex(c), t_ask, dt, latex(c), dt, vgh_ms, fmt_dec(v_ask), ans_d))

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n' +
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

