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


def bt_dang5_p2_b2_c2_hh12(self):
            # Khai báo biến
            x, y, z = symbols('x y z')

            # Random các giá trị cho đường thẳng d1
            x0_d1 = random.choice([3, -3, 1, -1, 2, -2])
            y0_d1 = random.choice([-1, 1, 2, -2, 3, -3])
            z0_d1 = random.choice([5, -5, 1, -1, 2, -2])
            a1_d1 = random.choice([1, -1, 2, -2, 3, -3])
            a2_d1 = random.choice([-1, 1, 2, -2, 3, -3])
            a3_d1 = random.choice([2, -2, 1, -1, 3, -3])

            # Random các giá trị cho đường thẳng d2
            x0_d2 = random.choice([4, -4, 1, -1, 2, -2])
            y0_d2 = random.choice([0, 1, -1, 2, -2])
            z0_d2 = random.choice([3, -3, 1, -1, 2, -2])
            a1_d2 = random.choice([-1, 1, 2, -2, 3, -3])
            a2_d2 = random.choice([2, -2, 1, -1, 3, -3])
            a3_d2 = random.choice([3, -3, 1, -1, 2, -2])

            # Tạo các vectơ chỉ phương
            u_d1 = [a1_d1, a2_d1, a3_d1]
            u_d2 = [a1_d2, a2_d2, a3_d2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho đường thẳng \\begin{center} $d_1: \\frac{x+%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$ và $d_2: \\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$. \\end{center}'''
            %(latex(x0_d1), latex(a1_d1), latex(y0_d1), latex(a2_d1), latex(z0_d1), latex(a3_d1),
            latex(x0_d2), latex(a1_d2), latex(y0_d2), latex(a2_d2), latex(z0_d2), latex(a3_d2)))

            ########################################################################Nhận biết ############################################
            # Tạo điểm M ngẫu nhiên
            t_nb = random.choice([1, -1, 2, -2])
            M_x = x0_d1 + a1_d1 * t_nb
            M_y = y0_d1 + a2_d1 * t_nb
            M_z = z0_d1 + a3_d1 * t_nb

            # Các đáp án
            nb_da_1_d = '\\True Điểm $M(%s;%s;%s)$ thuộc $d_1$' % (latex(-x0_d1), latex(y0_d1), latex(z0_d1))
            nb_da_1_s = 'Điểm $M(%s;%s;%s)$ thuộc $d_1$' % (latex(M_x), latex(M_y), latex(M_z))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thay tọa độ điểm $M(%s;%s;%s)$ vào phương trình đường thẳng $d_1$, ta thấy: \\\\
            $\\frac{%s+%s}{%s} = \\frac{%s-%s}{%s} = \\frac{%s-%s}{%s} \\Leftrightarrow %s=%s=%s$. \\\\
            Vậy điểm $M(%s;%s;%s)$ thuộc đường thẳng $d_1$.'''
            % (latex(-x0_d1), latex(y0_d1), latex(z0_d1),
            latex(-x0_d1), latex(x0_d1), latex(a1_d1),
            latex(y0_d1), latex(y0_d1), latex(a2_d1),
            latex(z0_d1), latex(z0_d1), latex(a3_d1),
            latex(0), latex(0), latex(0),
            latex(-x0_d1), latex(y0_d1), latex(z0_d1)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Thông hiểu ############################################
            # Tính cos góc giữa hai đường thẳng
            dot_product = u_d1[0]*u_d2[0] + u_d1[1]*u_d2[1] + u_d1[2]*u_d2[2]
            mag_d1 = sqrt(u_d1[0]**2 + u_d1[1]**2 + u_d1[2]**2)
            mag_d2 = sqrt(u_d2[0]**2 + u_d2[1]**2 + u_d2[2]**2)
            cos_alpha = Abs(dot_product) / (mag_d1 * mag_d2)

            # Các đáp án
            th_da_1_d = '\\True $\\cos(d_1,d_2)=%s$' % latex(cos_alpha)
            th_da_1_s = '$\\cos(d_1,d_2)=%s$' % latex(cos_alpha + 1/10)
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vectơ chỉ phương của $d_1$ là $\\vec{u_1}=(%s;%s;%s)$, của $d_2$ là $\\vec{u_2}=(%s;%s;%s)$. \\\\
            $\\cos(d_1,d_2) = \\frac{|\\vec{u_1} \\cdot \\vec{u_2}|}{|\\vec{u_1}| |\\vec{u_2}|} = \\frac{|(%s)(%s)+(%s)(%s)+(%s)(%s)|}{\\sqrt{%s^2+(%s)^2+%s^2} \\sqrt{%s^2+%s^2+%s^2}} = %s$.'''
            % (latex(a1_d1), latex(a2_d1), latex(a3_d1),
            latex(a1_d2), latex(a2_d2), latex(a3_d2),
            latex(a1_d1), latex(a1_d2), latex(a2_d1), latex(a2_d2), latex(a3_d1), latex(a3_d2),
            latex(a1_d1), latex(a2_d1), latex(a3_d1),
            latex(a1_d2), latex(a2_d2), latex(a3_d2),
            latex(cos_alpha)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Kiểm tra vị trí tương đối
            # vectơ chỉ phương không cùng phương
            cross_product = [
            u_d1[1] * u_d2[2] - u_d1[2] * u_d2[1],
            u_d1[2] * u_d2[0] - u_d1[0] * u_d2[2],
            u_d1[0] * u_d2[1] - u_d1[1] * u_d2[0]
            ]
            # vectơ nối hai điểm trên hai đường thẳng
            M1 = [-x0_d1, y0_d1, z0_d1]
            M2 = [x0_d2, y0_d2, z0_d2]
            vec_M1M2 = [M2[0] - M1[0], M2[1] - M1[1], M2[2] - M1[2]]
            # Tích hỗn hợp
            mixed_product = vec_M1M2[0]*cross_product[0] + vec_M1M2[1]*cross_product[1] + vec_M1M2[2]*cross_product[2]

            # Các đáp án
            if mixed_product != 0:
                vd_da_1_d = '\\True Hai đường thẳng $d_1$ và $d_2$ chéo nhau.'
                loigiai_vd_1 = ('''Ta có vectơ chỉ phương $\\vec{u_1}=(%s;%s;%s)$ và $\\vec{u_2}=(%s;%s;%s)$, chúng không cùng phương vì $\\frac{%s}{%s} \\neq \\frac{%s}{%s}$. \\\\
                            Lấy điểm $M_1(%s;%s;%s) \\in d_1$ và $M_2(%s;%s;%s) \\in d_2$. Ta có $\\vec{M_1M_2}=(%s;%s;%s)$. \\\\
                            Tích hỗn hợp $[\\vec{u_1},\\vec{u_2}]\\cdot\\vec{M_1M_2} = %s \\neq 0$. \\\\
                            Vậy hai đường thẳng $d_1$ và $d_2$ chéo nhau.'''
                            % (latex(a1_d1), latex(a2_d1), latex(a3_d1),
                               latex(a1_d2), latex(a2_d2), latex(a3_d2),
                               latex(a1_d1), latex(a1_d2), latex(a2_d1), latex(a2_d2),
                               latex(-x0_d1), latex(y0_d1), latex(z0_d1),
                               latex(x0_d2), latex(y0_d2), latex(z0_d2),
                               latex(vec_M1M2[0]), latex(vec_M1M2[1]), latex(vec_M1M2[2]),
                               latex(mixed_product)))
            else:
                vd_da_1_d = '\\True Hai đường thẳng $d_1$ và $d_2$ đồng phẳng'
                loigiai_vd_1 = ('''Ta có vectơ chỉ phương $\\vec{u_1}=(%s;%s;%s)$ và $\\vec{u_2}=(%s;%s;%s)$, chúng không cùng phương vì $\\frac{%s}{%s} \\neq \\frac{%s}{%s}$. \\\\
                            Lấy điểm $M_1(%s;%s;%s) \\in d_1$ và $M_2(%s;%s;%s) \\in d_2$. Ta có $\\vec{M_1M_2}=(%s;%s;%s)$. \\\\
                            Tích hỗn hợp $[\\vec{u_1},\\vec{u_2}]\\cdot\\vec{M_1M_2} = %s = 0$. \\\\
                            Vậy hai đường thẳng $d_1$ và $d_2$ đồng phẳng.'''
                            % (latex(a1_d1), latex(a2_d1), latex(a3_d1),
                               latex(a1_d2), latex(a2_d2), latex(a3_d2),
                               latex(a1_d1), latex(a1_d2), latex(a2_d1), latex(a2_d2),
                               latex(-x0_d1), latex(y0_d1), latex(z0_d1),
                               latex(x0_d2), latex(y0_d2), latex(z0_d2),
                               latex(vec_M1M2[0]), latex(vec_M1M2[1]), latex(vec_M1M2[2]),
                               latex(mixed_product)))
            vd_da_1_s = 'Hai đường thẳng $d_1$ và $d_2$ song song với nhau'
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # vectơ chỉ phương vuông góc với cả hai đường thẳng là tích có hướng
            u_vdc = [
                u_d1[1] * u_d2[2] - u_d1[2] * u_d2[1],
                u_d1[2] * u_d2[0] - u_d1[0] * u_d2[2],
                u_d1[0] * u_d2[1] - u_d1[1] * u_d2[0]
            ]

            # Các đáp án
            vdc_da_1_d = '\\True Đường thẳng vuông góc với hai đường thẳng $d_1,d_2$ có vectơ chỉ phương $\\vec{u}=(%s;%s;%s)$' % (latex(u_vdc[0]), latex(u_vdc[1]), latex(u_vdc[2]))
            vdc_da_1_s = 'Đường thẳng vuông góc với hai đường thẳng $d_1,d_2$ có vectơ chỉ phương $\\vec{u}=(%s;%s;%s)$' % (latex(u_vdc[0]+1), latex(u_vdc[1]), latex(u_vdc[2]))
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Một đường thẳng vuông góc với hai đường thẳng $d_1$ và $d_2$ thì vectơ chỉ phương của nó phải vuông góc với cả hai vectơ chỉ phương của $d_1$ và $d_2$. Do đó, vectơ chỉ phương của đường thẳng đó là tích có hướng của $\\vec{u_1}$ và $\\vec{u_2}$. \\\\
            $\\vec{u} = [\\vec{u_1},\\vec{u_2}] = (%s;%s;%s)$.'''
                % (latex(u_vdc[0]), latex(u_vdc[1]), latex(u_vdc[2])))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

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
            str(noidungcauhoi)+
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('--', '+').replace('+-', '-')
            return content   

