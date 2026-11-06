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


def bt_dang4_p2_b2_c1_ds12(self):
            # Khai báo biến
            a=randint(14,29)
            x=a
            s=(3*x**2)/2
            y=3*x/2
            s2=(x-4)*(y-6)
            s3=s-s2

            # Nội dung câu hỏi
            noidungcauhoi = ('Một trang sách có hình dạng hình chữ nhật có diện tích $%s$ cm$^2$. Giả sử trang sách được đặt dọc trên mặt bàn '
                            'và lề trên, lề dưới đều để $3 \\text{cm}$, lề trái và lề phải để $2 \\text{cm}$. Phần còn lại của trang sách được in chữ. Gọi $x$ là chiều rộng của trang sách.'
                            %(latex(s))
                            )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chiều dài của trang sách là $\\dfrac{%s}{x} \\text{cm}$'%(latex(s))
            nb_da_1_s = 'Chiều dài của trang sách là $(%s-x) \\text{cm}$'%(latex(s))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Chiều rộng của phần in chữ là $(x-4) \\text{cm}$'
            nb_da_2_s = 'Chiều rộng của phần in chữ là $(x-2) \\text{cm}$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Chiều dài của phần in chữ là $\\left(\\dfrac{%s}{x}-6\\right) \\text{cm}$'%(latex(s))
            nb_da_3_s = 'Chiều dài của phần in chữ là $\\left(\\dfrac{%s}{x}-3\\right) \\text{cm}$'%(latex(s))
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2,nb_da_3]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vì trang sách có hình dạng hình chữ nhật và có diện tích bằng $%s$cm$^2$ nên chiều dài của trang sách là $\\dfrac{%s}{x} \\text{cm}$.'%(latex(s),latex(s))
                        )
            loigiai_nb_2 = ('Vì lề trái và lề phải để $2\\text{cm}$ nên chiều rộng của phần in chữ là $(x-4) \\text{cm}$.'

                        )
            loigiai_nb_3 = ('Vì trang sách có hình dạng hình chữ nhật và có diện tích bằng $%s$cm$^2$ nên chiều dài của trang sách là $\\dfrac{%s}{x} \\text{cm}$.\\\\ \n'
                            'Mà phần lề trên, lề dưới đều để $3\\text{cm}$ nên chiều dài của phần in chữ là $\\left(\\dfrac{%s}{x}-6\\right) \\text{cm}$.'%(latex(s),latex(s),latex(s))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Diện tích phần in chữ là $(x-4)\\left(\\dfrac{%s}{x}-6\\right)$ cm$^2$'%(latex(s))
            th_da_1_s = 'Diện tích phần in chữ là $(x-2)\\left(\\dfrac{%s}{x}-3\\right)$ cm$^2$'%(latex(s))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Vì lề trái và lề phải để $2\\text{cm}$ nên chiều rộng của phần in chữ là $(x-4) \\text{cm}$.\\\\ \n'
                            'Trang sách có hình dạng hình chữ nhật và có diện tích bằng $%s$cm$^2$ nên chiều dài của trang sách là $\\dfrac{%s}{x} \\text{cm}$.\\\\ \n'
                            'Mà phần lề trên, lề dưới đều để $3\\text{cm}$ nên chiều dài của phần in chữ là $\\left(\\dfrac{%s}{x}-6\\right) \\text{cm}$.\\\\ \n '
                            'Suy ra diện tích phần in chữ là $S=(x-4)\\left(\\dfrac{%s}{x}-6\\right)$ cm$^2$.'

                            %(latex(s),latex(s),latex(s),latex(s))

                        )


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
            vd_da_1_d = '\\True Phần in chữ của trang sách có diện tích lớn nhất khi $x=%s \\text{cm}$'%(latex(x))
            vd_da_1_s = 'Phần in chữ của trang sách có diện tích lớn nhất khi $x=%s \\text{cm}$'%(latex(x+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Phần in chữ của trang sách có diện tích lớn nhất là $%s$ cm$^2$'%(latex(s2))
            vd_da_2_s = 'Phần in chữ của trang sách có diện tích lớn nhất là $%s$ cm$^2$'%(latex(s2+1))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Diện tích phần in chữ là $S=(x-4)\\left(\\dfrac{%s}{x}-6\\right)$cm$^2$.\\\\ \n'
                            'Ta có $S=(x-4)\\left(\\dfrac{%s}{x}-6\\right)=-6x-\\dfrac{%s}{x}+%s$. Suy ra $S\'=-6+\\dfrac{%s}{x^2}$ \n'
                            '$$S\'=0\\Leftrightarrow -6+\\dfrac{%s}{x^2}=0\\Rightarrow -6x^2+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=-%s\\text{(Loại)}}$$.\n'
                            'Bảng biến thiên\\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}\n'
                                '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                                '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                                '{$x$ /0.6, $S\'$ /0.8, $S$ /2.5}\n'
                                '{$0$,$%s$,$+\\infty$}\n'
                                '\\tkzTabLine{d,-,$0$,+}\n'
                                '\\tkzTabVar{D-/$-\\infty$,+/$%s$,-/$-6$}\n'
                            '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Từ bảng biến thiên ta thấy diện tích phần in chữ đạt giá trị lớn nhất bằng $%s$ cm$^2$ khi $x=%s \\text{cm}$.'

                            %(latex(s),latex(s),latex(4*s),latex(s+24),
                            latex(4*s),latex(4*s),latex(4*s),latex(a),latex(a),latex(a),latex(s2),latex(s2),latex(x)
                            )
                        )
            loigiai_vd_2 = ('Diện tích phần in chữ là $S=(x-4)\\left(\\dfrac{%s}{x}-6\\right)$cm$^2$.\\\\ \n'
                            'Ta có $S=(x-4)\\left(\\dfrac{%s}{x}-6\\right)=-6x-\\dfrac{%s}{x}+%s$.Suy ra $S\'=-6+\\dfrac{%s}{x^2}$ \n'
                            '$$S\'=0\\Leftrightarrow -6+\\dfrac{%s}{x^2}=0\\Rightarrow -6x^2+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=-%s\\text{(Loại)}}.$$\n'
                            'Bảng biến thiên\\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}\n'
                                '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                                '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                                '{$x$ /0.6, $S\'$ /0.8, $S$ /2.5}\n'
                                '{$0$,$%s$,$+\\infty$}\n'
                                '\\tkzTabLine{d,-,$0$,+}\n'
                                '\\tkzTabVar{D-/$-\\infty$,+/$%s$,-/$-6$}\n'
                            '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Từ bảng biến thiên ta thấy diện tích phần in chữ đạt giá trị lớn nhất bằng $%s$ cm$^2$ khi $x=%s \\text{cm}$.'

                            %(latex(s),latex(s),latex(4*s),latex(s+24),
                            latex(4*s),latex(4*s),latex(4*s),latex(a),latex(a),latex(a),latex(s2),latex(s2),latex(x)
                            )
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Khi phần in chữ có diện tích lớn nhất thì diện tích phần lề để trống bằng $%s$ cm$^2$'%(latex(s3))
            vdc_da_1_s = 'Khi phần in chữ có diện tích lớn nhất thì diện tích phần lề để trống bằng $%s$ cm$^2$'%(latex(s3+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Khi phần in chữ có diện tích lớn nhất thì diện tích phần lề để trống là\\\\ \n'
                            '\\hspace*{1cm}$%s-%s=%s$ cm$^2$.'
                            %(latex(s),latex(s2),latex(s3))
                        )


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
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.0','')
            return content

