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


def bt_dang3_p2_b2_c2_hh12(self):
            # Khai báo biến
            x, y, z, t, t_prime = symbols('x y z t t_prime')

            # Random các giá trị cho đường thẳng d
            x0_d = random.choice([3, -3, 4,-4, 2, -2])
            y0_d = random.choice([2, -2, 3, -3, 4,-4])
            z0_d = random.choice([3, -3, 4,-4, 2, -2])
            a1_d = random.choice([-4, 4, 2, -2, 3, -3])
            a2_d = random.choice([2, -2, 4, -4, 3, -3])
            a3_d = random.choice([3, -3, 4, -4, 2, -2])

            # Random các giá trị cho đường thẳng d'
            x0_d_prime = random.choice([3, -3, 4,-4, 2, -2])
            y0_d_prime = random.choice([3, -3, 4,-4, 2, -2])
            z0_d_prime = random.choice([3, -3, 4,-4, 2, -2])
            a1_d_prime = random.choice([3, -3, 4,-4, 2, -2])
            a2_d_prime = random.choice([3, -3, 4,-4, 2, -2])
            a3_d_prime = random.choice([3, -3, 4,-4, 2, -2])

            # Tạo các vectơ chỉ phương
            u_d = [a1_d, a2_d, a3_d]
            u_d_prime = [a1_d_prime, a2_d_prime, a3_d_prime]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho hai đường thẳng \\\\ $d:\\begin{cases}x=%s+%s t \\\\ y=%s+%s t \\\\ z=%s+%s t\\end{cases}$ và $d':\\begin{cases}x=%s+%s t' \\\\ y=%s+%s t' \\\\ z=%s+%s t'\\end{cases}$.'''
                             %(latex(x0_d), latex(a1_d), latex(y0_d), latex(a2_d), latex(z0_d), latex(a3_d),
                               latex(x0_d_prime), latex(a1_d_prime), latex(y0_d_prime), latex(a2_d_prime), latex(z0_d_prime), latex(a3_d_prime)))

            ########################################################################Nhận biết ############################################
            # Tạo điểm M ngẫu nhiên
            M_x = random.choice([x0_d, x0_d + a1_d, x0_d - a1_d, x0_d + 2*a1_d])
            M_y = random.choice([y0_d, y0_d + a2_d, y0_d - a2_d, y0_d + 2*a2_d])
            M_z = random.choice([z0_d, z0_d + a3_d, z0_d - a3_d, z0_d + 2*a3_d])

            # Các đáp án
            nb_da_1_d = '\\True Điểm $M(%s;%s;%s)$ thuộc đường thẳng $d$' % (latex(x0_d + a1_d), latex(y0_d + a2_d), latex(z0_d + a3_d))
            nb_da_1_s = 'Điểm $M(%s;%s;%s)$ thuộc đường thẳng $d$' % (latex(M_x), latex(M_y), latex(M_z))
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thay tọa độ điểm $M(%s;%s;%s)$ vào phương trình đường thẳng $d$: \\\\
                             $ \\begin{cases} x=%s+%s t \\\\
                             y=%s+%s t \\\\
                             z=%s+%s t \\end{cases}$
                             Ta có nghiệm $t=1$ nên điểm $M(%s;%s;%s)$ thuộc đường thẳng $d$.'''
                             % (latex(x0_d + a1_d), latex(y0_d + a2_d), latex(z0_d + a3_d),
                                latex(x0_d), latex(a1_d), latex(y0_d), latex(a2_d), latex(z0_d), latex(a3_d),
                                latex(x0_d + a1_d), latex(y0_d + a2_d), latex(z0_d + a3_d)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đường thẳng $d$ và $d\'$ lần lượt có vectơ chỉ phương $\\vec{u}=(%s;%s;%s)$ và $\\vec{u\'}=(%s;%s;%s)$' % (latex(a1_d), latex(a2_d), latex(a3_d), latex(a1_d_prime), latex(a2_d_prime), latex(a3_d_prime))
            th_da_1_s = 'Đường thẳng $d$ và $d\'$ lần lượt có vectơ chỉ phương $\\vec{u}=(%s;%s;%s)$ và $\\vec{u\'}=(%s;%s;%s)$' % (latex(a1_d + 1), latex(a2_d), latex(a3_d), latex(a1_d_prime), latex(a2_d_prime), latex(a3_d_prime))
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Từ phương trình của $d$ và $d'$, ta có thể dễ dàng xác định được các vectơ chỉ phương tương ứng là $\\vec{u}=(%s;%s;%s)$ và $\\vec{u\'}=(%s;%s;%s)$.'''
                                                                                                                                                                  % (latex(a1_d), latex(a2_d), latex(a3_d), latex(a1_d_prime), latex(a2_d_prime), latex(a3_d_prime)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################Vận dụng ############################################
            # Tính tích có hướng
            cross_product = [
                a2_d * a3_d_prime - a3_d * a2_d_prime,
                a3_d * a1_d_prime - a1_d * a3_d_prime,
                a1_d * a2_d_prime - a2_d * a1_d_prime
            ]

            # Các đáp án
            vd_da_1_d = '\\True Ta có $\\left[\\vec{u},\\vec{u\'}\\right]=(%s;%s;%s)$ nên giá của vectơ có tọa độ $(%s;%s;%s)$ vuông góc với hai đường thẳng $d$ và $d\'$' % (latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2]), latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2]))
            vd_da_1_s = 'Ta có $\\left[\\vec{u},\\vec{u\'}\\right]=(%s;%s;%s)$ nên giá của vectơ có tọa độ $(%s;%s;%s)$ song song với hai đường thẳng $d$ và $d\'$' % (latex(cross_product[0] + 1), latex(cross_product[1]), latex(cross_product[2]), latex(cross_product[0] + 1), latex(cross_product[1]), latex(cross_product[2]))
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''vectơ chỉ phương của $d$ là $\\vec{u}=(%s;%s;%s)$ và của $d\'$ là $\\vec{u\'}=(%s;%s;%s)$. Tích có hướng của hai vectơ này là $\\left[\\vec{u},\\vec{u\'}\\right]=(%s;%s;%s)$. vectơ này vuông góc với cả hai vectơ $\\vec{u}$ và $\\vec{u\'}$, do đó nó có giá vuông góc với cả hai đường thẳng $d$ và $d\'$.'''
                            % (latex(a1_d), latex(a2_d), latex(a3_d), latex(a1_d_prime), latex(a2_d_prime), latex(a3_d_prime),
                               latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2])))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################Vận dụng cao ############################################
            # Tạo vectơ chỉ phương ngẫu nhiên cho đường thẳng Delta
            Delta_a1 = random.choice([1, 2, 3])
            Delta_a2 = random.choice([2, 3, 1])
            Delta_a3 = random.choice([3, 1, 2])

            # Các đáp án
            vdc_da_1_d = '\\True Đường thẳng $\\Delta$ vuông góc với cả hai đường thẳng nên có vectơ chỉ phương là $(%s;%s;%s)$' % (latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2]))
            vdc_da_1_s = 'Đường thẳng $\\Delta$ vuông góc với cả hai đường thẳng nên có vectơ chỉ phương là $(%s;%s;%s)$' % (latex(Delta_a1), latex(Delta_a2), latex(Delta_a3))
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Một đường thẳng vuông góc với hai đường thẳng $d$ và $d'$ thì vectơ chỉ phương của nó phải cùng phương với tích có hướng của hai vectơ chỉ phương của $d$ và $d'$. \\\\
                             Ta có $\\left[\\vec{u},\\vec{u\'}\\right]=(%s;%s;%s)$. Vậy $\\Delta$ có vectơ chỉ phương là $(%s;%s;%s)$.'''
                                                          % (latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2]), latex(cross_product[0]), latex(cross_product[1]), latex(cross_product[2])))

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content    

