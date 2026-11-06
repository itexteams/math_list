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


def bt_dang2_p2_b5_c1_hh11(self):
            # Khai báo biến
            a=randint(1,20)
            # Nội dung câu hỏi
            noidungcauhoi = 'Cho hình lập phương $ABCD.A\'B\'C\'D\'$ có cạnh bằng $%s$. $O, O\'$ là tâm của hai đáy. Xét phép chiếu song song theo phương $AA\'$. \n' %(latex(a))

            hinhve = (   
                    '\\begin{center}   \n'
                        '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]   \n'
                            '\\clip(-1.1491334337871895,-0.9460019707744378) rectangle (6.1316817925591875,4.9130477625531235);  \n'
                            '\\draw (0.,0.)-- (3.,0.);  \n'
                            '\\draw (0.,0.)-- (0.,3.);  \n'
                            '\\draw (0.,3.)-- (3.,3.);  \n'
                            '\\draw (3.,3.)-- (3.,0.);  \n'
                            '\\draw (0.,3.)-- (2.,4.);  \n'
                            '\\draw (3.,3.)-- (5.,4.);  \n'
                            '\\draw (5.,4.)-- (5.,1.);  \n'
                            '\\draw (5.,1.)-- (3.,0.);  \n'
                            '\\draw (2.,4.)-- (5.,4.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,4.)-- (2.,1.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,1.)-- (5.,1.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,1.)-- (0.,0.);  \n'
                            '\\draw (2.,4.)-- (3.,3.);  \n'
                            '\\draw (0.,3.)-- (5.,4.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.,1.)-- (3.,0.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,1.);  \n'
                            '\\draw (1.4994780894978705,1.5) node[anchor=north west] {$A$};  \n'
                            '\\draw (-0.6,0.3496391639927138) node[anchor=north west] {$B$};  \n'
                            '\\draw (2.898311881016387,0) node[anchor=north west] {$C$};  \n'
                            '\\draw (5.030960120544617,1.3930315822565262) node[anchor=north west] {$D$};  \n'
                            '\\draw (2.1530315822565216,0.5) node[anchor=north west] {$O$};  \n'
                            '\\draw (1.6026707462492364,4.6) node[anchor=north west] {$A\'$};  \n'
                            '\\draw (-0.518511642528842,3.4568847172838475) node[anchor=north west] {$B\'$};  \n'
                            '\\draw (2.9900386870176012,3.2504994037811152) node[anchor=north west] {$C\'$};  \n'
                            '\\draw (5.019494269794466,4.4888112847975075) node[anchor=north west] {$D\'$};  \n'
                            '\\draw (2.393814448009709,4.1) node[anchor=north west] {$O\'$};  \n'
                        '\\end{tikzpicture}   \n'
                    '\\end{center}   \n'

                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hình chiếu của $C\'$ lên mặt phẳng $(ABCD)$ là $C$'
            nb_da_1_s = 'Hình chiếu của $C\'$ lên mặt phẳng $(ABCD)$ là $B$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Hình chiếu của $D\'$ lên mặt phẳng $(ABCD)$ là $D$'
            nb_da_2_s = 'Hình chiếu của $D\'$ lên mặt phẳng $(ABCD)$ là $A$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Hình chiếu của $C\'$ lên mặt phẳng $(ABCD)$ là $C$.'
                        )
            loigiai_nb_2 = ('Hình chiếu của $D\'$ lên mặt phẳng $(ABCD)$ là $D$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hình chiếu của $A\'B\'$ lên mặt phẳng $(ABCD)$ là $AB$'
            th_da_1_s = 'Hình chiếu của $A\'B\'$ lên mặt phẳng $(ABCD)$ là $AD$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Hình chiếu của $A\'C\'$ lên mặt phẳng $(ABCD)$ là $AC$'
            th_da_2_s = 'Hình chiếu của $A\'C\'$ lên mặt phẳng $(ABCD)$ là $AB$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Hình chiếu của $A\'B\'$ lên mặt phẳng $(ABCD)$ là $AB$.'
                        )
            loigiai_th_2 = ('Hình chiếu của $A\'C\'$ lên mặt phẳng $(ABCD)$ là $AC$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hình chiếu của $O\'$ lên mặt phẳng $(ABCD)$ là $O$'
            vd_da_1_s = 'Hình chiếu của $O\'$ lên mặt phẳng $(ABCD)$ là $A$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Hình chiếu của $B\'C\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(a))
            vd_da_2_s = 'Hình chiếu của $B\'C\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(Rational(a,2)))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Hình chiếu của $B\'D\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(a*sqrt(2)))
            vd_da_3_s = 'Hình chiếu của $B\'D\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(a))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True Hình chiếu của $O\'C\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(a*sqrt(2)/2))
            vd_da_4_s = 'Hình chiếu của $O\'C\'$ lên mặt phẳng $(ABCD)$ có độ dài là $%s$' %(latex(Rational(a,2)))
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2,vd_da_3,vd_da_4]

            # Nội dung lời giải
            loigiai_vd_1 = ('Hình chiếu của $O\'$ lên mặt phẳng $(ABCD)$ là $O$.'
                        )
            loigiai_vd_2 = ('Hình chiếu của $B\'C\'$ lên mặt phẳng $(ABCD)$ là đoạn $BC$ có độ dài là $%s$.' %(latex(a))
                        )
            loigiai_vd_3 = ('Hình chiếu của $B\'D\'$ lên mặt phẳng $(ABCD)$ là đoạn $BD$ có độ dài là $%s$' %(latex(a*sqrt(2)))
                        )
            loigiai_vd_4 = ('Hình chiếu của $O\'C\'$ lên mặt phẳng $(ABCD)$ là đoạn $OC$ có độ dài là $%s$' %(latex(a*sqrt(2)/2))
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2,loigiai_vd_3,loigiai_vd_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Hình chiếu của tam giác $O\'A\'B\'$ lên mặt phẳng $(ABCD)$ là tam giác $OAB$ có diện tích bằng $%s$' %(latex(Rational(a**2,4)))
            vdc_da_1_s = 'Hình chiếu của tam giác $O\'A\'B\'$ lên mặt phẳng $(ABCD)$ là tam giác $OAB$ có diện tích bằng $%s$' %(latex(Rational(a**2,2)))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Hình chiếu của tam giác $A\'B\'C\'$ lên mặt phẳng $(ABCD)$ là tam giác $ABC$ có diện tích bằng $%s$' %(latex(Rational(a**2,2)))
            vdc_da_2_s = 'Hình chiếu của tam giác $A\'B\'C\'$ lên mặt phẳng $(ABCD)$ là tam giác $ABC$ có diện tích bằng $%s$' %(latex(Rational(a**2,4)))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Diện tích đáy $ABCD$ là $%s$. \\\\ \n'
                            'Diện tích tam giác $OAB$ là $\\dfrac{1}{4} \\cdot %s=%s$.'
                            %(latex(a**2),latex(a**2),latex(Rational(a**2,4))
                        ))

            loigiai_vdc_2 = ('Diện tích đáy $ABCD$ là $%s$. \\\\ \n'
                            'Diện tích tam giác $ABC$ là $\\dfrac{1}{2} \\cdot %s=%s$.'
                            %(latex(a**2),latex(a**2),latex(Rational(a**2,2))
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

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
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

