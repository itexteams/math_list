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


def bt_dang4_p2_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo các tập hợp dựa trên đề bài
            # Tập S = {1, 2, ..., 20}
            S = list(range(1, 21))
            # Biến cố A: Chia hết cho 4
            A_set = [x for x in S if x % 4 == 0]
            # Biến cố B: Số nguyên tố (Lưu ý số 2 là số nguyên tố)
            B_set = [2, 3, 5, 7, 11, 13, 17, 19]
            # Biến cố C: Chia hết cho 6
            C_set = [x for x in S if x % 6 == 0]

            def list_to_latex(ls):
                return "{" + "; ".join(map(str, ls)) + "}"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp đựng $20$ tấm thẻ cùng loại được đánh số từ $1$ đến $20$. Rút ngẫu nhiên một tấm thẻ trong hộp. \\\\
            Gọi $A$ là biến cố: "Số ghi trên tấm thẻ là số chia hết cho $4$";\\\\
            $B$ là biến cố: "Số ghi trên tấm thẻ là số nguyên tố";\\\\
            $C$ là biến cố: "Số ghi trên tấm thẻ chia hết cho $6$".''')

            ########################################################################
            # Nhận biết - Phát biểu về tập hợp (a)
            ########################################################################
            # Đúng: Liệt kê đúng các phần tử (có số 2 trong B)
            nb_da_1_d = '\\True $A=\\{%s \\}, B=\\{%s \\}, C=\\{%s \\}$' % (list_to_latex(A_set), list_to_latex(B_set), list_to_latex(C_set))
            # Sai: Liệt kê thiếu số 2 trong tập B (giống trong ảnh)
            B_set_wrong = [3, 5, 7, 11, 13, 17, 19]
            nb_da_1_s = '$A=\\{%s \\}, B=\\{%s \\}, C=\\{%s \\}$' % (list_to_latex(A_set), list_to_latex(B_set_wrong), list_to_latex(C_set))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Các tấm thẻ được đánh số từ $1$ đến $20$ nên không gian mẫu là $S=\\{1; 2; \\dots; 20\\}$.\\\\
            + Các số chia hết cho $4$ là: $4; 8; 12; 16; 20$. Vậy $A=\\{%s \\}$.\\\\
            + Các số nguyên tố từ $1$ đến $20$ là: $2; 3; 5; 7; 11; 13; 17; 19$. Vậy $B=\\{%s \\}$.\\\\
            + Các số chia hết cho $6$ là: $6; 12; 18$. Vậy $C=\\{%s \\}$.''' 
                            % (list_to_latex(A_set), list_to_latex(B_set), list_to_latex(C_set)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Mối quan hệ A và B (b)
            ########################################################################
            # Đúng: A (các số chẵn > 2) và B (các số nguyên tố) -> A giao B = rỗng (vì A toàn bội của 4)
            th_da_1_d = '\\True $A$ và $B$ là hai biến cố xung khắc'
            th_da_1_s = '$A$ và $B$ không phải là hai biến cố xung khắc'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta thấy $A \\cap B = \\emptyset$ vì các phần tử của $A$ đều là hợp số (chia hết cho $4$), còn $B$ gồm các số nguyên tố. Do đó $A$ và $B$ là hai biến cố xung khắc.''')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Mối quan hệ B và C (c)
            ########################################################################
            # Đúng: B (nguyên tố) và C (chia hết cho 6) -> giao nhau bằng rỗng
            vd_da_1_d = '\\True $B$ và $C$ là hai biến cố xung khắc'
            vd_da_1_s = '$B$ và $C$ không phải là hai biến cố xung khắc'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta thấy $B \\cap C = \\emptyset$ vì các phần tử của $C$ là $\\{6; 12; 18\\}$ đều là hợp số, không có số nào thuộc tập hợp số nguyên tố $B$. Vậy $B$ và $C$ là hai biến cố xung khắc.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Mối quan hệ A và C (d)
            ########################################################################
            # Sai: A và C có chung số 12 nên không xung khắc
            vdc_da_1_d = '\\True $A$ và $C$ không phải là hai biến cố xung khắc'
            vdc_da_1_s = '$A$ và $C$ là hai biến cố xung khắc'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $A = \\{4; 8; 12; 16; 20\\}$ và $C = \\{6; 12; 18\\}$.\\\\
            Nhận thấy $A \\cap C = \\{12\\} \\neq \\emptyset$.\\\\
            Vì giao của hai biến cố khác rỗng nên $A$ và $C$ không phải là hai biến cố xung khắc.''')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_choice = random.choice(list_nb_da_1)
                th_da_choice = random.choice(list_th_da_1)
                vd_da_choice = random.choice(list_vd_da_1)
                vdc_da_choice = random.choice(list_vdc_da_1)

                answers = [nb_da_choice, th_da_choice, vd_da_choice, vdc_da_choice]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            shuffled_answers = answers
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

