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


def bt_dang5_p2_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến (mặc dù bài này chủ yếu dùng số nguyên)
            x = symbols('x')

            # B1: Nghiên cứu đề bài và khởi tạo thông số ngẫu nhiên
            # n1: Số đường A -> B
            # n2: Số đường B -> C
            # n3: Số đường A -> C trực tiếp
            n1 = random.randint(2, 4)
            n2 = random.randint(2, 4)
            n3 = random.randint(2, 4)

            # Tính toán các giá trị logic
            cach_A_C_ko_B = n3
            cach_A_C_qua_B = n1 * n2
            cach_A_B_ko_C = n1
            tong_A_C = n3 + (n1 * n2)
            cach_khu_hoi = tong_A_C * tong_A_C

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho các thành phố $A, B$ và $C$. Có $%s$ con đường từ $A$ đến $B$, $%s$ con đường từ $B$ đến $C$ và $%s$ con đường từ $A$ đến $C$.''' % (latex(n1), latex(n2), latex(n3)))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Có %s cách di chuyển từ thành phố $A$ đến thành phố $C$ mà không đi qua thành phố $B$' % (latex(cach_A_C_ko_B))
            nb_da_1_s = 'Có %s cách di chuyển từ thành phố $A$ đến thành phố $C$ mà không đi qua thành phố $B$' % (latex(n1 + n2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Lời giải nhận biết
            loigiai_nb_1 = ('''Các con đường đi từ $A$ đến $C$ mà không qua $B$ chính là các con đường nối trực tiếp $A$ và $C$. Theo giả thiết có $%s$ con đường như vậy.''' % (latex(n3)))

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Có %s cách di chuyển từ thành phố $A$ đến thành phố $C$ mà đi qua thành phố $B$' % (latex(cach_A_C_qua_B))
            th_da_1_s = 'Có %s cách di chuyển từ thành phố $A$ đến thành phố $C$ mà đi qua thành phố $B$' % (latex(n1 + n2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Lời giải thông hiểu
            loigiai_th_1 = ('''Việc di chuyển từ $A$ đến $C$ qua $B$ chia làm hai giai đoạn liên tiếp: \\\\
            Giai đoạn 1: Đi từ $A$ đến $B$ có $%s$ cách. \\\\
            Giai đoạn 2: Đi từ $B$ đến $C$ có $%s$ cách. \\\\
            Theo quy tắc nhân, ta có $%s \\times %s = %s$ cách.''' % (latex(n1), latex(n2), latex(n1), latex(n2), latex(cach_A_C_qua_B)))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Có %s cách đi từ thành phố $A$ đến thành phố $B$ mà không đi qua thành phố $C$' % (latex(cach_A_B_ko_C))
            vd_da_1_s = 'Có %s cách đi từ thành phố $A$ đến thành phố $B$ mà không đi qua thành phố $C$' % (latex(n1 + n3))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Lời giải vận dụng
            loigiai_vd_1 = ('''Các con đường đi trực tiếp từ $A$ đến $B$ không phụ thuộc vào thành phố $C$. Theo giả thiết có $%s$ con đường từ $A$ đến $B$.''' % (latex(n1)))

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = '\\True Có %s cách đi từ thành phố $A$ đến thành phố $C$ rồi quay trở lại thành phố $A$' % (latex(cach_khu_hoi))
            vdc_da_1_s = 'Có %s cách đi từ thành phố $A$ đến thành phố $C$ rồi quay trở lại thành phố $A$' % (latex(tong_A_C * 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Lời giải vận dụng cao
            loigiai_vdc_1 = ('''Số cách đi từ $A$ đến $C$ là: $%s + %s = %s$ cách (quy tắc cộng). \\\\
            Hành trình đi từ $A$ đến $C$ rồi quay về $A$ gồm hai công việc: \\\\
            Đi từ $A$ đến $C$: có $%s$ cách. \\\\
            Đi từ $C$ về $A$: có $%s$ cách. \\\\
            Theo quy tắc nhân, ta có $%s \\times %s = %s$ cách.''' 
            %(latex(cach_A_C_ko_B), latex(cach_A_C_qua_B), latex(tong_A_C), latex(tong_A_C), latex(tong_A_C), latex(tong_A_C), latex(tong_A_C), latex(cach_khu_hoi)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán danh sách cuối cùng
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Do chỉ có 1 câu mỗi mức độ nên không cần shuffle phức tạp như mẫu hàm số, 
            # nhưng vẫn tuân thủ cấu trúc zip/shuffle để đảm bảo tính tổng quát.
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất kết quả theo định dạng yêu cầu
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

