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


def bt_dang1_p2_b2_c4_ds12(self):
            # Khai báo biến
            n=randint(150,300)
            n1=randint(90,130)
            n2=n-n1

            t1=randint(60,80)
            t2=100-t1

            h1=(n1*t1/100)*100/(n1*t1/100+n2*t2/100)  
            number = Decimal(float(h1))  # Số cần làm tròn
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

            # Khai báo biến

            # Nội dung câu hỏi
            noidungcauhoi = ('Trước khi đưa một loại sản phẩm ra thị trường, người ta đã phỏng vấn ngẫu nhiên $%s$ khách hàng về sản phẩm đó$zz$ Kết quả thống kê như sau: có $%s$ người trả lời “sẽ mua”; có $%s$ người trả lời “không mua”$zz$ Kinh nghiệm cho thấy tỉ lệ khách hàng thực sự sẽ mua sản phẩm tương ứng với những cách trả lời “sẽ mua” và “không mua” lần lượt là $%s$phtram và $%s$phtram$zz$ \\\\ \n'
                            'Gọi $A$ là biến cố “Người được phỏng vấn thực sự sẽ mua sản phẩm”$zz$ \\\\ \n'
                            'Gọi $B$ là biến cố “Người được phỏng vấn trả lời sẽ mua sản phẩm”$zz$'
                            %(latex(n),latex(n1),latex(n2),latex(t1),latex(t2)
                            ))

            hinhve = (
                '\\begin{center} \n'
                    '\\begin{tabular}{|c|c|c|} \n'
                    '\\hline \n'
                    '\\diagbox{Thực tế }{Phỏng vấn} & Người mua thật & Người không mua thật \\\\ \n'
                    '\\hline \n'
                    'Người trả lời sẽ mua ($%s$) & $%s \\cdot %s=%s$ & $%s-%s=%s$ \\\\ \n'
                    '\\hline \n'
                    'Người trả lời sẽ không mua ($%s$) & $%s \\cdot %s=%s$ & $%s-%s=%s$ \\\\ \n'
                    '\\hline \n'
                '\\end{tabular} \n'
            '\\end{center} \n'
                %(latex(n1),latex(t1/100),latex(n1),latex(n1*t1/100),latex(n1),latex(n1*t1/100),latex(n1-n1*t1/100),
                latex(n2),latex(t2/100),latex(n2),latex(n2*t2/100),latex(n2),latex(n2*t2/100),latex(n2-n2*t2/100),
                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất $P(B) = %s$ và $P(\\overline{B}) = %s$' %(latex(Rational(n1,n)),latex(1-Rational(n1,n)))
            nb_da_1_s = 'Xác suất $P(B) = %s$ và $P(\\overline{B}) = %s$' %(latex(Rational(n1+1,n)),latex(1-Rational(n1+1,n)))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Số người trả lời “sẽ mua” là $%s$ nên $n(B) = %s$$zz$ Do đó \\\\ \n'
                            '\\hspace*{1cm} $P(B) = \\frac{%s}{%s} = %s$ và $P(\\overline{B}) = 1 - %s = %s$$zz$'
                            %(latex(n1),latex(n1),
                            latex(n1),latex(n),latex(Rational(n1,n)),latex(Rational(n1,n)),latex(1-Rational(n1,n))
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất có điều kiện $P(A|B) = %s$' %(latex(t1/100))
            th_da_1_s = 'Xác suất có điều kiện $P(A|B) = %s$' %(latex(1-t1/100))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $P(A|B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{n(A \\cap B)}{n(B)}$$zz$ \\\\ \n'
                            '\\hspace*{1cm} $A \\cap B$ là tập hợp các người trả lời sẽ mua và mua thật, do đó $n(A \\cap B) = %s$$zz$ \\\\ \n'
                            'Do đó, $P(A|B) = \\frac{%s}{%s} = %s$$zz$'
                            %(latex(n1*t1/100),
                            latex(n1*t1/100),latex(n1),latex(t1/100)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất $P(A) = %s$' %(latex(round((n1*t1/100+n2*t2/100)/n,1)))
            vd_da_1_s = 'Xác suất $P(A) = %s$' %(latex(0.9-round((n1*t1/100+n2*t2/100)/n,1)))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('$A$ là tập hợp các người mua thật, $n(A) = %s + %s = %s$. Do đó \\\\ \n'
                            '\\hspace*{1cm} $P(A) = \\frac{%s}{%s} = %s$$zz$'
                            %(latex(n1*t1/100),latex(n2*t2/100),latex(n1*t1/100+n2*t2/100),
                            latex(n1*t1/100+n2*t2/100),latex(n),latex(round((n1*t1/100+n2*t2/100)/n,1))
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Trong số những người được phỏng vấn thực sự sẽ mua sản phẩm có $%s$phtram người đã trả lời “sẽ mua” khi được phỏng vấn (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' %(latex(kq))
            vdc_da_1_s = 'Trong số những người được phỏng vấn thực sự sẽ mua sản phẩm có $%s$phtram người đã trả lời “sẽ mua” khi được phỏng vấn (kết quả tính theo phần trăm được làm tròn đến hàng đơn vị)' %(latex(kq-5))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Tổng số người thực sự mua sản phẩm là $%s$$zz$ Số người trả lời sẽ mua sản phẩm và thực sự mua là $%s$ người$zz$ \\\\ \n'
                            'Tỉ lệ người thực sự mua sản phẩm đã trả lời “sẽ mua” khi được phỏng vấn và người thực sự mua sản phẩm nói chung là $\\frac{%s}{%s} \\approx %s$phtram$zz$'
                        %(latex(n1*t1/100+n2*t2/100),latex(n1*t1/100),latex(n1*t1/100),latex(n1*t1/100+n2*t2/100),latex(kq)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'+str(hinhve)+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('phtram', '\\%').replace('.0', '').replace('.', ',').replace('$zz$', '.')
            return content

